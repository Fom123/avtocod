from typing import Any, Dict

from avtocod.methods.base import AvtocodMethod, Request
from avtocod.types.profile.profile import LoginData


class AuthLogin(AvtocodMethod[LoginData]):
    """Login in avtocod account"""

    email: str
    password: str

    __returning__ = LoginData

    def build_request(self) -> Request:
        data: Dict[str, Any] = self.dict()

        return Request(method="auth.login", params=data)
