from __future__ import annotations

import abc
from typing import Any, Dict, Generator, Generic, List, Optional, TypeVar, Union, cast

from pydantic import BaseConfig, BaseModel, Extra, Field
from pydantic.generics import GenericModel

from avtocod.exceptions import (
    AccountBanned,
    AvtocodException,
    CouldNotFindCar,
    InternalError,
    InvalidArgument,
    InvalidRequest,
    NotEnoughRepairBalance,
    ReportGenerationLimitExceeded,
    ReportNotFound,
    SessionExpired,
    SubscriptionNotFound,
    Unauthorized,
)
from avtocod.utils import generate_id
from avtocod.utils.utils import wrap_as_list

AvtocodType = TypeVar("AvtocodType", bound=Any)
ResponseType = Union[Any, AvtocodType, List[AvtocodType]]
JsonLikeDict = Dict[str, Any]
Data = Union[JsonLikeDict, List[JsonLikeDict]]

_sentinel = object()


class FullError(BaseModel):
    type: Optional[str] = None
    exp_class: Optional[str] = Field(alias="class", default=None)
    message: Optional[str] = None
    code: Union[Optional[int], Optional[str]] = None


class AvtocodError(BaseModel):
    code: int
    message: str
    data: Union[Optional[List[FullError]], Optional[FullError]] = None


class Response(GenericModel, Generic[AvtocodType]):
    jsonrpc: str
    result: Optional[AvtocodType] = None
    error: Optional[AvtocodError] = None
    id: str

    def check_error(self) -> Response[AvtocodType]:
        error = self.error

        if not error:
            return self

        if error.code == 17002:
            raise NotEnoughRepairBalance("There are not enough balance")
        elif error.code == 18001:
            raise ReportNotFound("Report with this UUID not found")
        elif error.code == 19004:
            raise SubscriptionNotFound("Subscription not found.")
        elif error.code == 22002:
            raise ReportGenerationLimitExceeded("Report generation limit exceeded")
        elif error.code == 22004:
            raise AccountBanned("Account was banned.")
        elif error.code == 24001:
            raise CouldNotFindCar("Couldn't find car.")
        elif error.code == -32600:
            raise InvalidRequest("Invalid request.")
        elif error.code == -32602:
            error_message = "\n".join([str(data.message) for data in wrap_as_list(error.data)])
            raise InvalidArgument(f"{error_message}")
        if error.code == -32603:
            if data := cast(FullError, error.data):
                if data.code == 0:
                    # if we did not authorize
                    raise SessionExpired("Session expired")
                elif data.code == 401:
                    # if login/password wrong
                    raise Unauthorized("User not authenticated")
                raise InternalError(data.message)
        raise AvtocodException(f"Unknown error! {error.json()}")


class JsonrpcRequest(BaseModel):
    """Generate method to avtocod json_rpc 2.0 API."""

    jsonrpc: str = "2.0"
    """JSON-RPC version."""

    id: str = Field(default_factory=generate_id("natural"))
    """"Unique identifier for the request."""

    method: str
    """json_rpc method"""

    params: Dict[str, Any] = Field(default_factory=dict)
    """dictionary of params"""

    class Config(BaseConfig):
        arbitrary_types_allowed = True


class Request(BaseModel):
    data: Data

    http_method: str
    """HTTP method."""

    @classmethod
    def from_jsonrpc(
        cls, request: Union[JsonrpcRequest, List[JsonrpcRequest]], http_method: str
    ) -> Request:
        http_request = cls(
            data=request.dict()
            if not isinstance(request, list)
            else [request_.dict() for request_ in request],
            http_method=http_method,
        )
        if http_method:
            http_request.http_method = http_method
        return http_request

    class Config(BaseConfig):
        arbitrary_types_allowed = True


class AvtocodMethod(abc.ABC, BaseModel, Generic[AvtocodType]):
    class Config(BaseConfig):
        extra = Extra.allow
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        orm_mode = True

    @property
    def http_method(self) -> str:
        return "POST"

    @property
    @abc.abstractmethod
    def __returning__(self) -> type:
        pass

    @abc.abstractmethod
    def build_jsonrpc_request(self) -> JsonrpcRequest:
        pass

    def build_request(self) -> Request:
        return Request.from_jsonrpc(self.build_jsonrpc_request(), http_method=self.http_method)

    def dict(self, **kwargs: Any) -> Any:
        # override dict of pydantic.BaseModel to overcome exporting exclude field
        exclude = kwargs.pop("exclude", set())

        return super().dict(exclude=exclude, **kwargs)

    def build_response(self, data: Data) -> ResponseType[AvtocodType]:
        response = Response[self.__returning__](**data)  # type: ignore

        response.check_error()

        result = cast(AvtocodType, response.result)
        parsed_by_model_json = self.on_response_parse(result)
        if parsed_by_model_json is not _sentinel:
            return parsed_by_model_json
        return result

    @classmethod
    def on_response_parse(cls, response: AvtocodType) -> Union[Any, AvtocodType]:
        return _sentinel

    def __await__(self) -> Generator[Any, None, AvtocodType]:
        """Required for manually calling method and testing"""
        from avtocod import AvtoCod

        avtocod = AvtoCod.get_current(no_error=False)
        return avtocod(self).__await__()  # type: ignore
