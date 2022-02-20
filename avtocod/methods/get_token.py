from typing import cast

from avtocod.methods.base import AvtocodMethod, AvtocodType, Request
from avtocod.types.profile.token import Token


class GetToken(AvtocodMethod[str]):
    __returning__ = Token

    def build_request(self) -> Request:
        return Request(method="token.get")

    @classmethod
    def on_response_parse(cls, response: AvtocodType) -> str:
        return cast(str, response.token)
