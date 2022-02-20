import abc
import uuid
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union, cast

from pydantic import BaseConfig, BaseModel, Extra, Field
from pydantic.generics import GenericModel

from avtocod.exceptions import (
    AccountBanned,
    AvtocodException,
    CouldNotFindCar,
    InvalidRequest,
    NotEnoughRepairBalance,
    ReportNotFound,
    SessionExpired,
    SubscriptionNotFound,
    Unauthorized,
)

AvtocodType = TypeVar("AvtocodType", bound=Any)
_sentinel = object()


class FullError(BaseModel):
    type: Optional[str] = None
    exp_class: Optional[str] = Field(alias="class", default=None)
    message: Optional[str] = None
    code: Optional[int] = None


class AvtocodError(BaseModel):
    code: int
    message: str
    data: Union[List[FullError], Optional[FullError]] = None


class Response(GenericModel, Generic[AvtocodType]):
    jsonrpc: str
    result: Optional[AvtocodType] = None
    error: Optional[AvtocodError] = None
    id: str


class Request(BaseModel):
    """Generate method to avtocod json_rpc 2.0 API."""

    id: str = str(uuid.uuid4())
    """Unique id of every request"""
    method: str
    """json_rpc method"""
    params: Optional[Dict[str, Any]]
    """dictionary of params"""

    class Config(BaseConfig):
        arbitrary_types_allowed = True


class AvtocodMethod(abc.ABC, BaseModel, Generic[AvtocodType]):
    class Config(BaseConfig):
        extra = Extra.allow
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        orm_mode = True

    @property
    @abc.abstractmethod
    def __returning__(self) -> type:
        pass

    @abc.abstractmethod
    def build_request(self) -> Union[List[Request], Request]:
        pass

    @staticmethod
    def check_error(parsed_data: Response[AvtocodType]) -> Response[AvtocodType]:
        if not (error := parsed_data.error):
            return parsed_data
        if error.code == -32603:
            if data := error.data:
                if data.code == 0:  # type: ignore # if we did not authorize
                    raise SessionExpired("Session expired")
                elif data.code == 401:  # type: ignore # if login/password wrong
                    raise Unauthorized("User not authenticated")
        elif error.code == -32600:
            raise InvalidRequest("Invalid request.")
        elif error.code == 19004:
            raise SubscriptionNotFound("Subscription not found.")
        elif error.code == 22004:
            raise AccountBanned("Account was banned.")
        elif error.code == 24001:
            raise CouldNotFindCar("Couldn't find car.")
        elif error.code == 17002:
            raise NotEnoughRepairBalance("There are not enough balance")
        elif error.code == 18001:
            raise ReportNotFound("Report with this UUID not found")

        raise AvtocodException(f"Unknown error! {error.json()}")

    def dict(self, **kwargs: Any) -> Any:
        # override dict of pydantic.BaseModel to overcome exporting exclude field
        exclude = kwargs.pop("exclude", set())

        return super().dict(exclude=exclude, **kwargs)

    def build_response(self, data: Dict[str, Any]) -> AvtocodType:
        response = Response[self.__returning__](**data)  # type: ignore

        self.check_error(response)

        result = cast(AvtocodType, response.result)
        parsed_by_model_json = self.on_response_parse(result)
        if parsed_by_model_json is not _sentinel:
            return parsed_by_model_json  # type: ignore
        return result

    @classmethod
    def on_response_parse(cls, response: AvtocodType) -> Union[Any, AvtocodType]:
        return _sentinel
