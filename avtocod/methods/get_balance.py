from avtocod.methods.base import AvtocodMethod, Request
from avtocod.types.profile.profile import Balance


class GetBalance(AvtocodMethod[Balance]):
    """Get the current avtocod repair balance"""

    __returning__ = Balance

    def build_request(self) -> Request:
        return Request(method="profile.balance")
