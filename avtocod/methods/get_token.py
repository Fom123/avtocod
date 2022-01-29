from avtocod.methods.base import AvtocodMethod, Request
from avtocod.types.profile.token import Token


class GetToken(AvtocodMethod[Token]):
    __returning__ = Token

    def build_request(self) -> Request:
        return Request(method="token.get")
