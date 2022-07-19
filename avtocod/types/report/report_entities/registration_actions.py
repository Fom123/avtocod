from typing import Any, List, Optional

from pydantic import Field

from avtocod.types import AvtocodObject
from avtocod.types.report.report_entities.identifiers import Vehicle
from avtocod.types.reusable import DateStartEnd, DateUpdate


class Geo(AvtocodObject):
    city: Optional[str] = Field(None, description="Город")
    house: Optional[str] = Field(None, description="Дом")
    region: Optional[str] = Field(None, description="Регион")
    street: Optional[str] = Field(None, description="Улица")


class Owner(AvtocodObject):
    org: List[Any] = Field(default_factory=list, description="Организация")
    type: Optional[str] = None
    phone_number: Optional[str] = None


class RegistrationItem(AvtocodObject):
    id: Optional[int] = Field(None, alias="_id")
    geo: Optional[Geo] = None
    code: Optional[str] = Field(None, description="Код проверки")
    date: Optional[DateStartEnd] = None
    type: Optional[str] = Field(None, description="Тип проверки")
    owner: Optional[Owner] = Field(None, description="Владелец")
    reg_num: Optional[str] = Field(None, description="Регистрационный номер")
    actuality: List[Any] = Field(default_factory=list, description="Актуальность")
    attributes: List[Any] = Field(default_factory=list, description="Атрибуты")
    identifiers: Optional[Vehicle] = None
    usage_allowed: Optional[bool] = None


class RegistrationActions(AvtocodObject):
    date: Optional[DateUpdate] = None
    count: Optional[int] = None
    items: Optional[List[RegistrationItem]] = None
