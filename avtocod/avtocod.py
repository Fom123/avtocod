from __future__ import annotations

import asyncio
import logging
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncGenerator,
    Awaitable,
    List,
    Optional,
    Type,
    TypeVar,
    overload,
)

from .exceptions import ValidationError
from .methods.authorization import AuthLogin
from .methods.base import AvtocodMethod, AvtocodType, ResponseType
from .methods.create_report import CreateReport
from .methods.get_balance import GetBalance
from .methods.get_report import GetReport
from .methods.get_reports import GetReports
from .methods.get_token import GetToken
from .methods.order_repair import AdditionalUpgrade
from .methods.upgrade_report import UpgradeReport
from .mixins import ContextInstanceMixin, DataMixin
from .session.aiohttp import AiohttpSession
from .session.base import BaseSession
from .types.profile.profile import BalanceItem, LoginData
from .types.report.generation import ReviewGeneration, ReviewUpgrade
from .types.report.query_type import QueryType
from .types.report.report import Report
from .types.report.reports import BaseReport, Filters, Pagination, Sort
from .utils.utils import pipeline_support

logger = logging.getLogger(__name__)

AvtoCodT = TypeVar("AvtoCodT", bound="AvtoCod")
PipelineT = TypeVar("PipelineT", bound="Pipeline")

if TYPE_CHECKING:
    from .pipeline import Pipeline


class AvtoCod(ContextInstanceMixin["AvtoCod"], DataMixin):
    def __init__(
        self,
        token: Optional[str] = None,
        *,
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

    @overload
    def __call__(
        self,
        method: AvtocodMethod[AvtocodType],
        request_timeout: Optional[int] = None,
    ) -> Awaitable[AvtocodType]:
        ...

    @overload
    def __call__(
        self,
        method: Any,
        request_timeout: Optional[int] = None,
    ) -> Awaitable[ResponseType[AvtocodType]]:
        ...

    def __call__(
        self,
        method: AvtocodMethod[AvtocodType],
        request_timeout: Optional[int] = None,
    ) -> Awaitable[ResponseType[AvtocodType]]:
        """
        Call API method
        :param method:
        :return:
        """
        return self.session(self, method, timeout=request_timeout)

    @property
    def token(self) -> Optional[str]:
        return self._token

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
        from .pipeline import Pipeline

        return Pipeline(session=self.session, token=self.token)

    @classmethod
    async def from_credentials(
        cls: Type[AvtoCodT],
        email: str,
        password: str,
        request_timeout: Optional[int] = None,
        *args: Any,
        **kwargs: Any,
    ) -> AvtoCodT:
        """Method for creating avtocod instance from credentials

        :param email: email of avtocod account
        :param password: password of avtocod account
        :param request_timeout: timeout for request
        :param args: args for creating instance
        :param kwargs: kwargs for creating instance

        :return: avtocod instance
        """

        avtocod = cls(*args, **kwargs)
        
        login_data = await avtocod.login(email, password, request_timeout=request_timeout)

        return cls(
            login_data.token, session=kwargs.pop("session", avtocod.session), *args, **kwargs
        )

    async def login(
        self, email: str, password: str, request_timeout: Optional[int] = None
    ) -> LoginData:
        """
        Login in avtocod account using credentials

        :param email: email of avtocod account
        :param password: password of avtocod account
        :param request_timeout: timeout for request

        :return: LoginData
        """
        call = AuthLogin(email=email, password=password)

        data = await self(method=call, request_timeout=request_timeout)

        logger.info("Successful log in. Email: %s", data.email)

        return data

    async def iter_reports(
        self,
        sort: Optional[Sort] = None,
        filters: Optional[Filters] = None,
        limit: int = 0,
        delay_between_request: int = 5,
        request_timeout: Optional[int] = None,
    ) -> AsyncGenerator[BaseReport, None]:
        """
        Iterate over all reports in avtocod account

        :param sort: sort by this field
        :param filters: filter by this field
        :param limit: limit of reports to fetch
        :param delay_between_request: delay between requests
        :param request_timeout: timeout for request
        """
        current = 0
        total = limit or (1 << 31) - 1
        limit = min(20, total)
        page = 1

        while True:
            reports = await self.get_reports(
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

            if delay_between_request:
                await asyncio.sleep(delay_between_request)

    @pipeline_support
    def get_token(self, request_timeout: Optional[int] = None) -> Awaitable[str]:
        """TODO: what is this method for?"""
        call = GetToken()
        return self(method=call, request_timeout=request_timeout)

    @pipeline_support
    def create_report(
        self, query: str, query_type: QueryType, request_timeout: Optional[int] = None
    ) -> Awaitable[ReviewGeneration]:
        """
        Method to create report

        :param query: car number. Can be vin, body, grz
        :param query_type: the type of the query, must be one of the following VIN/BODY/GRZ
        :param request_timeout: timeout for request

        :return: Awaitable[ReviewGeneration]
        """
        call = CreateReport(query=query, type=query_type)
        return self(method=call, request_timeout=request_timeout)

    @pipeline_support
    def get_report(self, uuid: str, request_timeout: Optional[int] = None) -> Awaitable[Report]:
        """
        Get the avtocod report, can be used without authorization.

        :param uuid: Unique id of report
        :param request_timeout: timeout for request

        :return: Awaitable[Report]
        """
        call = GetReport(uuid=uuid)
        return self(method=call, request_timeout=request_timeout)

    @pipeline_support
    def upgrade_report(
        self, uuid: str, request_timeout: Optional[int] = None
    ) -> Awaitable[ReviewUpgrade]:
        """Upgrade the report to the full version

        :param uuid: Unique id of report
        :param request_timeout: timeout for request

        :return: Awaitable[ReviewUpgrade]
        """

        call = UpgradeReport(uuid=uuid)
        return self(method=call, request_timeout=request_timeout)

    @pipeline_support
    def get_reports(
        self,
        pagination: Optional[Pagination] = None,
        sort: Optional[Sort] = None,
        filters: Optional[Filters] = None,
        request_timeout: Optional[int] = None,
    ) -> Awaitable[List[BaseReport]]:
        """
        Get the list of reports, if pagination weren't set,
        then by default it will return 10 reports from first page

        :param pagination: pagination object
        :param sort: sort object
        :param filters: filters object
        :param request_timeout: timeout for request

        :return: Awaitable[List[Reports]]
        """
        call = GetReports(pagination=pagination, sort=sort, filters=filters)
        return self(method=call, request_timeout=request_timeout)

    @pipeline_support
    def get_account_info(
        self, request_timeout: Optional[int] = None
    ) -> Awaitable[List[BalanceItem]]:
        """
        Get the account info, can be used without authorization.

        :param request_timeout: timeout of how much request can handle

        :return: Awaitable[List[BalanceItem]]
        """
        call = GetBalance()
        return self(method=call, request_timeout=request_timeout)

    @pipeline_support
    def upgrade_review_repair(
        self, uuid: str, product_uuid: str, request_timeout: Optional[int] = None
    ) -> Awaitable[ReviewUpgrade]:
        """Order the repair of the report

        :param uuid: Unique id of report
        :param product_uuid: Unique id of product which have enough balance
        (can be found in the account_info)
        :param request_timeout: timeout for request

        :return: Awaitable[ReviewUpgrade]
        """

        call = AdditionalUpgrade(report_uuid=uuid, product_uuid=product_uuid)
        return self(method=call, request_timeout=request_timeout)
