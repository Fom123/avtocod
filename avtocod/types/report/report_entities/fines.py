from typing import Any, List, Optional

from pydantic import Field

from avtocod.types import AvtocodObject
from avtocod.types.reusable import DateEndPercent, DateEvent, DateUpdate, Name, Total


class Location(AvtocodObject):
    raw: Optional[str] = Field(None, alias="Местонахождение")


class Fssp(AvtocodObject):
    is_proceed: Optional[bool] = False


class Number(AvtocodObject):
    number: Optional[int] = None


class Payment(AvtocodObject):
    purpose: Optional[str] = None


class Article(AvtocodObject):
    code: Optional[str] = None
    description: Optional[str] = None


class User(AvtocodObject):
    kpp: Optional[str] = None
    tin: Optional[str] = None
    name: Optional[str] = None


class Bank(AvtocodObject):
    bik: Optional[str] = Field(None, description="БИК банка")
    name: Optional[str] = Field(None, description="Наименование банка")
    account: Optional[Number] = Field(None, description="Номер счета")


class Wire(AvtocodObject):
    kbk: Optional[str] = None
    bank: Optional[Bank] = None
    user: Optional[User] = None
    okato: Optional[int] = None
    payment: Optional[Payment] = None


class FinesItems(AvtocodObject):
    id: Optional[int] = Field(None, alias="_id")
    uid: Optional[str] = None
    date: Optional[DateEvent] = None
    fssp: Optional[Fssp] = None
    wire: Optional[Wire] = None
    amount: Optional[Total] = None
    photos: Optional[List[Any]] = None
    vendor: Optional[Name] = None
    article: Optional[Article] = None
    is_paid: Optional[bool] = None
    discount: Optional[DateEndPercent] = None
    location: Optional[Location] = None
    description: Optional[str] = None
    need_payment: Optional[bool] = None
    uin: Optional[str] = None


class Fines(AvtocodObject):
    date: Optional[DateUpdate] = None
    count: Optional[int] = None
    items: Optional[List[FinesItems]] = None
    has_fines: Optional[bool] = None
    comment: Optional[str] = Field(None, alias="_comment")
