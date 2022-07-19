from typing import List, cast

from avtocod.methods.base import AvtocodMethod, AvtocodType, JsonrpcRequest
from avtocod.types.profile.profile import Balance, BalanceItem


class GetBalance(AvtocodMethod[List[BalanceItem]]):
    """Get the current avtocod repair balance"""

    __returning__ = Balance

    def build_jsonrpc_request(self) -> JsonrpcRequest:
        return JsonrpcRequest(method="profile.balance")

    @classmethod
    def on_response_parse(cls, response: AvtocodType) -> List[BalanceItem]:
        return cast(List[BalanceItem], response.balance)
