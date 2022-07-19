from typing import Any, Dict

from avtocod.methods.base import AvtocodMethod, JsonrpcRequest
from avtocod.types.profile.profile import LoginData


class AuthLogin(AvtocodMethod[LoginData]):
    """Login in avtocod account"""

    email: str
    password: str

    __returning__ = LoginData

    def build_jsonrpc_request(self) -> JsonrpcRequest:
        data: Dict[str, Any] = self.dict()

        return JsonrpcRequest(method="auth.login", params=data)
