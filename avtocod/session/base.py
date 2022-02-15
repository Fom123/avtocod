import abc
import datetime
import json
from types import TracebackType
from typing import Any, Callable, Dict, Final, Optional, Type, Union

from avtocod.methods.base import AvtocodMethod, AvtocodType, Response
from avtocod.types.base import UNSET, utcformat
from ..exceptions import (
    AccountBanned,
    AvtocodException,
    CouldNotFindCar,
    InvalidRequest,
    NetworkError,
    NotEnoughRepairBalance,
    ReportNotFound,
    SessionExpired,
    SubscriptionNotFound,
    Unauthorized,
)

_JsonLoads = Callable[..., Any]
_JsonDumps = Callable[..., str]

DEFAULT_TIMEOUT: Final[float] = 30.0
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
        timeout: float = DEFAULT_TIMEOUT,
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
    ) -> AvtocodType:
        return await self._make_request(self.api, method, timeout=timeout)

    def check_response(
        self, method: AvtocodMethod[AvtocodType], content_type: str, content: str
    ) -> Response[AvtocodType]:
        if content_type != "application/json":
            raise NetworkError(f'Invalid response with content type {content_type}: "{content}"')

        try:
            json_data = self.json_loads(content)
        except ValueError:
            json_data = {}

        parsed_data = method.build_response(json_data)

        if not (error := parsed_data.error):
            return parsed_data
        if error.code == -32603:
            if data := error.data:
                if data.code == 0:  # if we did not authorize
                    raise SessionExpired("Session expired")
                elif data.code == 401:  # if login/password wrong
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

        raise AvtocodException(f"Unknown error! {json_data}")

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
    ) -> AvtocodType:
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
