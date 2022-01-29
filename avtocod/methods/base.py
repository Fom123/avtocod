import abc
import uuid
from typing import Any, Dict, Generic, Optional, TypeVar

from pydantic import BaseConfig, BaseModel, Extra, Field
from pydantic.generics import GenericModel

AvtocodType = TypeVar("AvtocodType", bound=Any)


class FullError(BaseModel):
    type: Optional[str] = None
    exp_class: Optional[str] = Field(alias="class", default=None)
    message: Optional[str] = None
    code: Optional[int] = None


class AvtocodError(BaseModel):
    code: int
    message: str
    data: Optional[FullError] = None


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
    def build_request(self) -> Request:
        pass

    def dict(self, **kwargs: Any) -> Any:
        # override dict of pydantic.BaseModel to overcome exporting exclude field
        exclude = kwargs.pop("exclude", set())

        return super().dict(exclude=exclude, **kwargs)

    def build_response(self, data: Dict[str, Any]) -> Response[AvtocodType]:
        return Response[self.__returning__](**data)  # type: ignore
