import logging
from typing import Awaitable, Callable, Tuple

from avtocod import AvtoCod
from avtocod.exceptions import PipelineException, SessionExpired
from avtocod.methods import AvtocodMethod, AvtocodType
from avtocod.methods.base import ResponseType
from avtocod.session.middlewares.base import BaseRequestMiddleware, NextRequestMiddlewareType

logger = logging.getLogger(__name__)


class LoginPasswordGetter:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    async def __call__(self) -> Tuple[str, str]:
        return self.login, self.password


class ReLoginMiddleware(BaseRequestMiddleware):
    def __init__(self, login_password_getter: Callable[[], Awaitable[Tuple[str, str]]]):
        self.login_password_getter = login_password_getter

    async def __call__(
        self,
        make_request: NextRequestMiddlewareType[AvtocodType],
        avtocod: AvtoCod,
        method: AvtocodMethod[AvtocodType],
    ) -> ResponseType[AvtocodType]:
        async def relogin() -> None:
            logger.info("Session expired, getting login and password")

            login, password = await self.login_password_getter()

            logger.info("Successfully got login and password, logging in")

            # not changing instance of AvtoCod, creating a new one
            nonlocal avtocod
            avtocod = await AvtoCod.from_credentials(login, password, session=avtocod.session)

            logger.info("Successfully logged in.")

        try:
            return await make_request(avtocod, method)
        except SessionExpired:
            await relogin()
            return await make_request(avtocod, method)
        except PipelineException as e:
            session_expired = [
                (index, r_or_e.avtocod_method)
                for index, r_or_e in enumerate(e.results_and_error)
                if isinstance(r_or_e.result, SessionExpired)
            ]
            for index, avtocod_method in session_expired:
                await relogin()
                e.results_and_error[index].result = await make_request(avtocod, avtocod_method)
            return [r.result for r in e.results_and_error]
