import abc
import datetime
import json
from functools import partial
from types import TracebackType
from typing import TYPE_CHECKING, Any, Callable, Dict, Final, List, Optional, Type, Union

from avtocod.methods.base import (
    AvtocodMethod,
    AvtocodType,
    Data,
    JsonLikeDict,
    Request,
    ResponseType,
)
from avtocod.types.base import UNSET, AvtocodObject, utcformat
from .middlewares.base import RequestMiddlewareType
from ..consts import AVTOCOD_API, HEADERS
from ..exceptions import NetworkError

if TYPE_CHECKING:
    from .. import AvtoCod

_JsonLoads = Callable[..., Any]
_JsonDumps = Callable[..., str]

DEFAULT_TIMEOUT: Final[int] = 30


# source:
# https://github.com/aiogram/aiogram/blob/c7058584219a2138bab44b7760604bf62783aaf5/aiogram/client/session/base.py#L63
class BaseSession(abc.ABC):
    def __init__(
        self,
        api: str = AVTOCOD_API,
        json_loads: _JsonLoads = json.loads,
        json_dumps: _JsonDumps = json.dumps,
        timeout: int = DEFAULT_TIMEOUT,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        :param api: Avtocod API URL
        :param json_loads: JSON loader
        :param json_dumps: JSON dumper
        :param timeout: Session scope request timeout
        """
        self.api = api
        self.json_loads = json_loads
        self.json_dumps = json_dumps
        self.timeout = timeout
        self.headers = HEADERS.copy()
        self.headers.update(headers or {})

        self._middlewares: List[RequestMiddlewareType[AvtocodObject]] = []

    async def __call__(
        self,
        avtocod: "AvtoCod",
        method: AvtocodMethod[AvtocodType],
        timeout: Optional[int] = UNSET,
    ) -> ResponseType[AvtocodType]:
        middleware = partial(self.make_request, timeout=timeout)
        for m in reversed(self._middlewares):
            middleware = partial(m, middleware)  # type: ignore
        return await middleware(avtocod, method)

    def check_response(
        self, method: AvtocodMethod[AvtocodType], content_type: str, content: str
    ) -> ResponseType[AvtocodType]:
        if content_type != "application/json":
            raise NetworkError(f'Invalid response with content type {content_type}: "{content}"')

        try:
            json_data = self.json_loads(content)
        except ValueError:
            json_data = {}

        return method.build_response(json_data)

    @abc.abstractmethod
    async def close(self) -> None:
        """
        Close client session
        """

    @abc.abstractmethod
    async def make_request(
        self,
        avtocod: "AvtoCod",
        method: AvtocodMethod[AvtocodType],
        timeout: Optional[int] = UNSET,
    ) -> ResponseType[AvtocodType]:
        """
        Making request to avtocod api
        """

    def prepare_value(self, value: Any) -> Union[str, int, bool, Any]:
        """
        Prepare value before send
        """
        if isinstance(value, str):
            return value
        if isinstance(value, (list, dict)):
            return self.clean_json(value)
        if isinstance(value, datetime.timedelta):
            now = datetime.datetime.now()
            return utcformat(now + value)
        if isinstance(value, datetime.datetime):
            return utcformat(value)
        return value

    def clean_json(self, value: Any) -> Any:
        """
        Clean data before send
        """
        if isinstance(value, list):
            return [self.prepare_value(v) for v in value if v is not None]
        elif isinstance(value, dict):
            return {k: self.prepare_value(v) for k, v in value.items() if v is not None}
        return value

    def build_data(self, request: Request) -> Data:
        is_batch = isinstance(request.data, list)

        def build(request_: JsonLikeDict) -> JsonLikeDict:
            data_ = {}
            for key, value in request_.items():
                if value is None or value is UNSET:
                    continue
                data_[key] = self.prepare_value(value)
            return data_

        if is_batch:
            return [build(data) for data in request.data]  # type: ignore
        else:
            return build(request.data)  # type: ignore

    def middleware(
        self, middleware: RequestMiddlewareType[AvtocodObject]
    ) -> RequestMiddlewareType[AvtocodObject]:
        self._middlewares.append(middleware)
        return middleware

    async def __aenter__(self) -> "BaseSession":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        await self.close()
