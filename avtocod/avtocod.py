from __future__ import annotations

import logging
from typing import Any, Final, List, Optional, Tuple

from .exceptions import ValidationError
from .methods.authorization import AuthLogin
from .methods.base import AvtocodMethod, AvtocodType
from .methods.create_report import CreateReport
from .methods.get_balance import GetBalance
from .methods.get_report import GetReport
from .methods.get_reports_list import GetReviewsList
from .methods.get_token import GetToken
from .methods.order_repair import AdditionalUpgrade
from .methods.upgrade_report import UpgradeReport
from .mixins import ContextInstanceMixin, DataMixin
from .session.aiohttp import AiohttpSession
from .session.base import BaseSession
from .types.profile.profile import Balance, LoginData
from .types.review.generation import ReviewGeneration, ReviewUpgrade
from .types.review.query_type import QueryType
from .types.review.review import Review
from .types.review.reviews_list import Filters, Pagination, ReviewsList, Sort

logger = logging.getLogger(__name__)

MAX_REPORT_LIMIT: Final[int] = 20
POLLING_DELAY: Final[int] = 5
POLLING_ERROR: Final[int] = 30


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
        return await self.session(method, timeout=request_timeout)

    @property
    def token(self) -> Optional[str]:
        return self._token

    @token.setter
    def token(self, token: str) -> None:
        self._token = token
        self.validate_token()
        self._update_auth_headers()

    @token.deleter
    def token(self) -> None:
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

    def pipeline(self, transaction: bool = True, shard_hint: Optional[str] = None) -> None:  # TODO
        """
        Return a new pipeline object that can queue multiple commands for
        later execution. ``transaction`` indicates whether all commands
        should be executed atomically.
        """
        raise NotImplementedError

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

    async def get_token(self, request_timeout: Optional[int] = None) -> str:
        """Idk what is that, something like temporary token? Expires in 30 second and cannot be used for api calls"""
        call = GetToken()
        data = await self(method=call, request_timeout=request_timeout)
        return data.token

    async def create_report(
        self, query: str, query_type: QueryType, request_timeout: Optional[int] = None
    ) -> ReviewGeneration:
        """
        Method to create report

        :param query: car number. Can be vin, body, grz
        :param query_type: the type of the query, must be one of the following VIN/BODY/GRZ
        :param request_timeout: timeout of how much request can handle

        :return: uuid of review on success
        """
        call = CreateReport(query=query, type=query_type)
        return await self(method=call, request_timeout=request_timeout)

    async def get_report(self, uuid: str, request_timeout: Optional[int] = None) -> Review:
        """
        Get the avtocod report, can be used without authorization.

        :param uuid: Unique id of report
        :param request_timeout: timeout of how much request can handle
        """
        call = GetReport(uuid=uuid)
        return await self(method=call, request_timeout=request_timeout)

    async def upgrade_report(
        self, uuid: str, request_timeout: Optional[int] = None
    ) -> ReviewUpgrade:
        call = UpgradeReport(uuid=uuid)
        return await self(method=call, request_timeout=request_timeout)

    async def get_reports_list(
        self,
        pagination: Optional[Pagination] = None,
        sort: Optional[Sort] = None,
        filters: Optional[Filters] = None,
        request_timeout: Optional[int] = None,
    ) -> List[ReviewsList]:
        """
        Get the list of reports, if pagination weren't set,
        then by default it will return 10 reports from first page
        """
        call = GetReviewsList(pagination=pagination, sort=sort, filters=filters)
        data = await self(method=call, request_timeout=request_timeout)
        return [report for report in data.reports_list]

    async def get_balance(self, request_timeout: Optional[int] = None) -> Tuple[int, str]:
        """
        Get the balance and account id information

        :return: tuple of balance and account_id
        """
        call = GetBalance()
        data: Balance = await self(method=call, request_timeout=request_timeout)
        balance = data.balance[0].count
        account_id = data.balance[0].product_uuid
        return balance, account_id

    async def upgrade_repair(
        self, uuid: str, request_timeout: Optional[int] = None
    ) -> ReviewUpgrade:
        balance, account_id = await self.get_balance()
        call = AdditionalUpgrade(report_uuid=uuid, product_uuid=account_id)
        return await self(method=call, request_timeout=request_timeout)
