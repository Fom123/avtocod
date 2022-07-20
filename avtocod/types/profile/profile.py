from typing import List, Optional

from avtocod.types.base import AvtocodObject


class BalanceItem(AvtocodObject):
    product_uuid: str
    count: int


class Balance(AvtocodObject):
    balance: List[BalanceItem]


class LoginData(AvtocodObject):
    uuid: str
    token: str
    email: str
    phone: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
