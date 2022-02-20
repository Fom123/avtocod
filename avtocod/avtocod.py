from __future__ import annotations

import logging
import typing
import warnings
from types import TracebackType
from typing import (
    Any,
    Awaitable,
    Final,
    Generator,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
)

from .exceptions import ValidationError
from .methods.authorization import AuthLogin
from .methods.base import AvtocodMethod, AvtocodType
from .methods.create_report import CreateReport
from .methods.get_balance import GetBalance
from .methods.get_report import GetReport
from .methods.get_reports_list import GetReviewsList
from .methods.get_token import GetToken
from .methods.multirequest import MultiRequest
from .methods.order_repair import AdditionalUpgrade
from .methods.upgrade_report import UpgradeReport
from .mixins import ContextInstanceMixin, DataMixin
from .session.aiohttp import AiohttpSession
from .session.base import BaseSession
from .types.profile.profile import BalanceItem, LoginData
from .types.review.generation import ReviewGeneration, ReviewUpgrade
from .types.review.query_type import QueryType
from .types.review.review import Review
from .types.review.reviews_list import Filters, Pagination, ReviewsList, Sort

logger = logging.getLogger(__name__)

MAX_REPORT_LIMIT: Final[int] = 20
POLLING_DELAY: Final[int] = 5
POLLING_ERROR: Final[int] = 30

_Avtocod = TypeVar("_Avtocod", bound="AvtoCod")


class AvtoCod(ContextInstanceMixin["AvtoCod"], DataMixin):
    def __init__(
        self,
        token: Optional[str] = None,
        session: Optional[BaseSession] = None,
    ):

        self._token = token
        self.session = session if session is not None else AiohttpSession()

        if self._token:
            self.validate_token()
            self._update_auth_headers()

    def __hash__(self) -> int:
        """
        Get hash for the token
        :return:
        """
        return hash(self.token)

    def __eq__(self, other: Any) -> bool:
        """
        Compare current avtocod instance with another
        :param other:
        :return:
        """
        if not isinstance(other, AvtoCod):
            return False
        return hash(self) == hash(other)

    async def __call__(
        self,
        method: AvtocodMethod[AvtocodType],
        request_timeout: Optional[int] = None,
    ) -> AvtocodType:
        """
        Call API method
        :param method:
        :return:
        """
        response, errors = await self.session(method, timeout=request_timeout)
        # cuz avtocod instances can return only one response. Made for pipeline compatibility
        if errors:
            raise errors[0][1]
        return cast(AvtocodType, response)

    @property
    def token(self) -> Optional[str]:
        return self._token

    @token.setter
    def token(self, token: str) -> None:
        warnings.warn(
            "`AvtoCod.token = ...` is deprecated and will be removed in version 0.3.0. "
            "Create new instance of `AvtoCod` instead",
            DeprecationWarning,
            stacklevel=2,
        )
        self._token = token
        self.validate_token()
        self._update_auth_headers()

    @token.deleter
    def token(self) -> None:
        warnings.warn(
            "`del AvtoCod.token` is deprecated and will be removed in version 0.3.0. "
            "Create new instance of `AvtoCod` instead",
            DeprecationWarning,
            stacklevel=2,
        )
        self._token = None
        self._update_auth_headers()

    def _update_auth_headers(self) -> None:
        self.session.headers["Authorization"] = f"Bearer {self._token}"

    def validate_token(self) -> bool:
        if not isinstance(self._token, str):
            raise ValidationError(
                "Token is invalid! " f"It must be 'str' type instead of {type(self._token)} type."
            )

        if any(x.isspace() for x in self._token):
            raise ValidationError("Token is invalid! It can't contains spaces.")
        return True

    def pipeline(self) -> "Pipeline":
        """
        Return a new pipeline object that can queue multiple commands for
        later execution.
        """
        return Pipeline(token=self.token, session=self.session)

    @classmethod
    async def from_credentials(
        cls,
        email: str,
        password: str,
        request_timeout: Optional[int] = None,
        *args: Any,
        **kwargs: Any,
    ) -> AvtoCod:
        avtocod = cls(*args, **kwargs)

        login_data = await avtocod.login(email, password, request_timeout=request_timeout)

        return cls(login_data.token, *args, **kwargs)

    @classmethod
    async def from_token(cls, token: str, *args: Any, **kwargs: Any) -> AvtoCod:
        """
        Same as `AvtoCod(token)`
        """
        return cls(token, *args, **kwargs)

    async def login(
        self, email: str, password: str, request_timeout: Optional[int] = None
    ) -> LoginData:
        """Login in avtocod account using credentials"""
        call = AuthLogin(email=email, password=password)

        data = await self(method=call, request_timeout=request_timeout)

        logger.info("Successful log in. Email: %s", data.email)

        return data

    def get_token(self, request_timeout: Optional[int] = None) -> Awaitable[str]:
        """Idk what is that, something like temporary token? Expires in 30 second and cannot be used for api calls"""
        call = GetToken()
        return self(method=call, request_timeout=request_timeout)

    def create_report(
        self, query: str, query_type: QueryType, request_timeout: Optional[int] = None
    ) -> Awaitable[ReviewGeneration]:
        """
        Method to create report

        :param query: car number. Can be vin, body, grz
        :param query_type: the type of the query, must be one of the following VIN/BODY/GRZ
        :param request_timeout: timeout of how much request can handle

        :return: uuid of review on success
        """
        call = CreateReport(query=query, type=query_type)
        return self(method=call, request_timeout=request_timeout)

    def get_report(self, uuid: str, request_timeout: Optional[int] = None) -> Awaitable[Review]:
        """
        Get the avtocod report, can be used without authorization.

        :param uuid: Unique id of report
        :param request_timeout: timeout of how much request can handle
        """
        call = GetReport(uuid=uuid)
        return self(method=call, request_timeout=request_timeout)

    def upgrade_report(
        self, uuid: str, request_timeout: Optional[int] = None
    ) -> Awaitable[ReviewUpgrade]:
        call = UpgradeReport(uuid=uuid)
        return self(method=call, request_timeout=request_timeout)

    def get_reports_list(
        self,
        pagination: Optional[Pagination] = None,
        sort: Optional[Sort] = None,
        filters: Optional[Filters] = None,
        request_timeout: Optional[int] = None,
    ) -> Awaitable[List[ReviewsList]]:
        """
        Get the list of reports, if pagination weren't set,
        then by default it will return 10 reports from first page
        """
        call = GetReviewsList(pagination=pagination, sort=sort, filters=filters)
        return self(method=call, request_timeout=request_timeout)

    async def get_balance(self, request_timeout: Optional[int] = None) -> Tuple[int, str]:
        """
        Get the balance and account id information

        :return: tuple of balance and account_id
        """
        warnings.warn(
            "`AvtoCod.get_balance(...)` is deprecated and will be removed in 0.3.0, "
            "use `AvtoCod.get_account_info(...) instead`",
            DeprecationWarning,
            stacklevel=2,
        )
        call = GetBalance()
        balance: List[BalanceItem] = await self(method=call, request_timeout=request_timeout)

        return balance[0].count, balance[0].product_uuid

    def get_account_info(
        self, request_timeout: Optional[int] = None
    ) -> Awaitable[List[BalanceItem]]:
        """
        Get the list of balance and account id information

        :return: tuple of balance and account_id
        """
        call = GetBalance()
        return self(method=call, request_timeout=request_timeout)

    async def upgrade_repair(
        self, uuid: str, request_timeout: Optional[int] = None
    ) -> ReviewUpgrade:
        warnings.warn(
            "`AvtoCod.upgrade_repair(...)` is deprecated and will be removed in version 0.3.0. "
            "Use `AvtoCod.upgrade_review_repair(...)` instead",
            DeprecationWarning,
            stacklevel=2,
        )
        balance, account_id = await self.get_balance()
        call = AdditionalUpgrade(report_uuid=uuid, product_uuid=account_id)
        return await self(method=call, request_timeout=request_timeout)

    def upgrade_review_repair(
        self, uuid: str, product_uuid: str, request_timeout: Optional[int] = None
    ) -> Awaitable[ReviewUpgrade]:
        """ """
        call = AdditionalUpgrade(report_uuid=uuid, product_uuid=product_uuid)
        return self(method=call, request_timeout=request_timeout)


class Pipeline(AvtoCod):
    def __init__(self, *, token: Optional[str] = None, session: Optional[BaseSession] = None):
        super().__init__(token, session)

        # self.response_callbacks = response_callbacks
        self.method_stack: List[Tuple[AvtocodMethod[Any], Optional[int]]] = []

    @typing.no_type_check
    def __call__(
        self,
        method: AvtocodMethod[Any],
        request_timeout: Optional[int] = None,
    ) -> Union[Pipeline, Awaitable[Pipeline]]:
        self.method_stack.append((method, request_timeout))
        return self

    async def __aenter__(self) -> Pipeline:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        await self.reset()

    async def _async_self(self) -> Pipeline:
        return self

    def __await__(self) -> Generator[Any, None, Pipeline]:
        return self._async_self().__await__()

    def __len__(self) -> int:
        return len(self.method_stack)

    def __bool__(self) -> bool:
        return True

    async def reset(self) -> None:
        self.method_stack = []

    async def _execute_transaction(
        self,
        methods: List[AvtocodMethod[AvtocodType]],
        raise_on_error: bool = False,
        request_timeout: Optional[int] = None,
    ) -> Any:

        responses, errors = await self.session(
            MultiRequest(methods=methods), timeout=request_timeout
        )

        assert isinstance(responses, list)
        # put any api errors into the response
        for i, e in errors:
            responses[i] = e

        if raise_on_error and errors:
            raise errors[0][1]

        return responses

    async def execute(
        self, raise_on_error: bool = True, request_timeout: Optional[int] = None
    ) -> Any:
        """Execute all the commands in the current pipeline"""
        if not self.method_stack:
            return []

        if request_timeout is None:
            request_timeout = min(
                (timeout for request, timeout in self.method_stack if isinstance(timeout, int)),
                default=self.session.timeout,
            )
        methods = [method for method, timeout in self.method_stack]

        try:
            return await self._execute_transaction(methods, raise_on_error, request_timeout)
        finally:
            await self.reset()
