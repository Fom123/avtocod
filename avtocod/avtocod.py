from __future__ import annotations

import asyncio
import logging
import warnings
from types import TracebackType
from typing import (
    Any,
    AsyncGenerator,
    Awaitable,
    Generator,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
)

from .exceptions import AvtocodException, ValidationError
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

AvtoCodT = TypeVar("AvtoCodT", bound="AvtoCod")
PipelineT = TypeVar("PipelineT", bound="Pipeline")


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
        response, errors = await self.session(self, method, timeout=request_timeout)
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
        if not isinstance(self.token, str):
            raise ValidationError(
                "Token is invalid! " f"It must be 'str' type instead of {type(self.token)} type."
            )

        if any(x.isspace() for x in self.token):
            raise ValidationError("Token is invalid! It can't contains spaces.")
        return True

    def pipeline(self) -> Pipeline:
        """
        Return a new pipeline object that can queue multiple commands for
        later execution.
        """
        return Pipeline(token=self.token, session=self.session)

    @classmethod
    async def from_credentials(
        cls: Type[AvtoCodT],
        email: str,
        password: str,
        request_timeout: Optional[int] = None,
        *args: Any,
        **kwargs: Any,
    ) -> AvtoCodT:
        avtocod = cls(*args, **kwargs)

        login_data = await avtocod.login(email, password, request_timeout=request_timeout)

        return cls(login_data.token, *args, **kwargs)

    @classmethod
    async def from_token(cls: Type[AvtoCodT], token: str, *args: Any, **kwargs: Any) -> AvtoCodT:
        """
        Same as `AvtoCod(token)`
        """
        warnings.warn(
            "`AvtoCod.from_token(...)` is deprecated and will be removed in version 0.4.0. "
            "Do AvtoCod(token=...) instead",
            DeprecationWarning,
            stacklevel=2,
        )
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

        :return: uuid of reviews_entity on success
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

    async def iter_reports_list(
        self,
        sort: Optional[Sort] = None,
        filters: Optional[Filters] = None,
        limit: int = 0,
        delay_between_request: int = 5,
        request_timeout: Optional[int] = None,
    ) -> AsyncGenerator[ReviewsList, None]:
        current = 0
        total = limit or (1 << 31) - 1
        limit = min(20, total)
        page = 1

        while True:
            reports = await self.get_reports_list(
                pagination=Pagination(page=page, limit=limit),
                sort=sort,
                filters=filters,
                request_timeout=request_timeout,
            )
            if not reports:
                break

            page += 1

            for report in reports:
                yield report
                current += 1

                if current >= total:
                    return
            await asyncio.sleep(delay_between_request)

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

        self.method_stack: List[Tuple[AvtocodMethod[Any], Optional[int]]] = []

    def __call__(  # type: ignore[override]
        self,
        method: AvtocodMethod[Any],
        request_timeout: Optional[int] = None,
    ) -> Pipeline:
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

    async def _async_self(self: PipelineT) -> PipelineT:
        return self

    def __await__(self: PipelineT) -> Generator[Any, None, PipelineT]:
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
    ) -> List[Union[AvtocodType, AvtocodException]]:

        responses, errors = await self.session(
            self, MultiRequest(methods=methods), timeout=request_timeout
        )

        assert isinstance(responses, List)
        # put any api errors into the response
        for i, e in errors:
            responses.insert(i, e)

        if raise_on_error and errors:
            raise errors[0][1]

        return cast(List[Union[AvtocodType, AvtocodException]], responses)

    async def execute(
        self, raise_on_error: bool = True, request_timeout: Optional[int] = None
    ) -> List[Union[AvtocodType, AvtocodException]]:
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
