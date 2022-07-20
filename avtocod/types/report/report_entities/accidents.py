from typing import Any, Dict, List, Optional

from pydantic import Field

from avtocod.types import AvtocodObject
from avtocod.types.reusable import DateDate, DateUpdate, Name, Total


class Geo(AvtocodObject):
    city: Optional[str] = None
    house: Optional[str] = None
    region: Optional[str] = None
    street: Optional[str] = None


class ItemVehicle(AvtocodObject):
    year: Optional[int] = None
    brand: Optional[Name] = None
    model: Optional[Name] = None


class ItemsOfPledges(AvtocodObject):
    id: Optional[int] = Field(None, alias="_id")
    geo: Optional[Geo] = None
    org: List[Any] = Field(default_factory=list)
    type: Optional[str] = None
    state: Optional[str] = None
    damage: Any = None
    number: Optional[Any] = None
    vehicle: Optional[ItemVehicle] = None
    accident: Optional[DateDate] = None
    actuality: Optional[DateDate] = None
    participants: Optional[Total] = None
    other_participants: List[Any] = Field(default_factory=list)


class Pledges(AvtocodObject):
    date: Optional[DateUpdate] = None
    count: Optional[int] = None
    items: Optional[List[ItemsOfPledges]] = None
    comment: Optional[str] = Field(None, alias="_comment")


class Accidents(AvtocodObject):
    history: Optional[Pledges] = None
    insurance: Optional[Dict[str, Any]] = None
    has_accidents: Optional[bool] = None
