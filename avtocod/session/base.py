import abc
import datetime
import json
from types import TracebackType
from typing import Any, Callable, Dict, Final, List, Optional, Tuple, Type, Union, cast

from avtocod.methods.base import AvtocodMethod, AvtocodType
from avtocod.types.base import UNSET, utcformat

from ..exceptions import AvtocodException, NetworkError
from ..methods.multirequest import MultiRequest

_JsonLoads = Callable[..., Any]
_JsonDumps = Callable[..., str]

DEFAULT_TIMEOUT: Final[int] = 30
AVTOCOD_API: str = "https://api-profi.avtocod.ru/rpc"
HEADERS: Dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    "Accept": "application/json",
    "Content-Type": "application/json",
}


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
        self.headers = headers if headers else HEADERS.copy()

    async def __call__(
        self, method: AvtocodMethod[AvtocodType], timeout: Optional[int] = UNSET
    ) -> Tuple[Union[List[AvtocodType], AvtocodType], List[Tuple[int, AvtocodException]]]:
        return await self._make_request(self.api, method, timeout=timeout)

    @staticmethod
    def wrap_multirequest(
        method: Union[AvtocodMethod[AvtocodType], List[AvtocodMethod[AvtocodType]]],
        data: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        if isinstance(method, MultiRequest):
            return cast(List[Dict[str, Any]], data)
        return [data]

    @staticmethod
    def unwrap_multirequest(method: AvtocodMethod[AvtocodType], data: List[Any]) -> Any:
        if isinstance(method, MultiRequest):
            return data
        return data[0]

    def check_response(
        self, method: AvtocodMethod[AvtocodType], content_type: str, content: str
    ) -> Tuple[Union[List[AvtocodType], AvtocodType], List[Tuple[int, AvtocodException]]]:
        if content_type != "application/json":
            raise NetworkError(f'Invalid response with content type {content_type}: "{content}"')

        try:
            json_data = self.json_loads(content)
        except ValueError:
            json_data = {}

        parsed_responses: List[Optional[AvtocodType]] = []
        errors: List[Tuple[int, AvtocodException]] = []

        for index, data in enumerate(self.wrap_multirequest(method, json_data)):
            try:
                parsed_responses.append(method.build_response(data))
            except AvtocodException as e:
                parsed_responses.append(None)
                errors.append(
                    (
                        index,
                        e,
                    )
                )

        return (
            self.unwrap_multirequest(method, parsed_responses),
            errors,
        )

    @abc.abstractmethod
    async def close(self) -> None:
        """
        Close client session
        """

    @abc.abstractmethod
    async def _make_request(
        self,
        url: str,
        method: AvtocodMethod[AvtocodType],
        timeout: Optional[int] = UNSET,
    ) -> Tuple[Union[List[AvtocodType], AvtocodType], List[Tuple[int, AvtocodException]]]:
        """
        Making request to avtocod api
        Errors code:
            19004 - Subscription ended
            22004 - Account banned
            24001 - Vehicle not found
            -32603 - User not authenticated
            -32600 - Invalid Request
            -32602 - Invalid Argument
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

    async def __aenter__(self) -> "BaseSession":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        await self.close()
