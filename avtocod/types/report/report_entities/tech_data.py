from typing import Any, List, Optional

from pydantic import Field

from avtocod.types.base import AvtocodObject
from avtocod.types.reusable import DateUpdate, Name, StartEnd, TypeA


class OriginalNormalizedName(AvtocodObject):
    original: Optional[str] = None
    normalized: Optional[str] = None


class Logotype(AvtocodObject):
    uri: Optional[str] = None


class Standarts(AvtocodObject):
    emission: Optional[List[Any]] = None


class Chassis(AvtocodObject):
    number: Optional[str] = None
    comment: Optional[str] = Field(None, alias="_comment")


class Transmission(AvtocodObject):
    comment: Optional[str] = Field(None, alias="_comment")


class Color(AvtocodObject):
    name: Optional[str] = None
    type: Optional[str] = None


class Body(AvtocodObject):
    color: Optional[Color] = None
    number: Optional[str] = None
    comment: Optional[str] = Field(None, alias="_comment")


class Drive(AvtocodObject):
    type: Optional[str] = None
    type_id: Optional[str] = None
    comment: Optional[str] = Field(None, alias="_comment")


class Model(AvtocodObject):
    id: Optional[str] = None
    name: Optional[OriginalNormalizedName] = None
    comment: Optional[str] = Field(None, alias="_comment")


class Brand(AvtocodObject):
    id: Optional[str] = None
    name: Optional[OriginalNormalizedName] = None
    logotype: Optional[Logotype] = None
    comment: Optional[str] = Field(None, alias="_comment")


class Type(AvtocodObject):
    code: Optional[str] = None
    name: Optional[str] = None
    type_id: Optional[str] = None
    comment: Optional[str] = Field(None, alias="_comment")


class Wheel(AvtocodObject):
    comment: Optional[str] = Field(None, alias="_comment")
    position: Optional[str] = None
    position_id: Optional[str] = None
    position_code: Optional[str] = None


class Fuel(AvtocodObject):
    type: Optional[str] = None
    type_id: Optional[str] = None


class Power(AvtocodObject):
    hp: Optional[int] = None
    kw: Optional[int] = None


class Engine(AvtocodObject):
    fuel: Optional[Fuel] = None
    power: Optional[Power] = None
    number: Optional[str] = None
    volume: Optional[int] = None
    model: Optional[Name] = None
    standarts: Optional[Standarts] = None

    comment: Optional[str] = Field(None, alias="_comment")


class Weight(AvtocodObject):
    max: Optional[int] = None
    netto: Optional[int] = None
    comment: Optional[str] = Field(None, alias="_comment")


class BodiesModification(AvtocodObject):
    id: Optional[int] = None
    name: Optional[str] = None
    drive: Optional[TypeA] = None
    engine: Optional[Engine] = None
    transmission: Optional[TypeA] = None


class Bodies(AvtocodObject):
    id: Optional[int] = None
    type: Optional[str] = None
    modifications: List[BodiesModification] = Field(default_factory=list)


class Generations(AvtocodObject):
    id: Optional[int] = None
    name: Optional[str] = None
    years: Optional[StartEnd] = None
    bodies: List[Bodies] = Field(default_factory=list)
    is_restyling: Optional[bool] = None


class TechData(AvtocodObject):
    type: Optional[Type] = None
    year: Optional[int] = None
    brand: Optional[Brand] = None
    drive: Optional[Drive] = None
    model: Optional[Model] = None
    wheel: Optional[Wheel] = None
    engine: Optional[Engine] = None
    weight: Optional[Weight] = None

    body: Optional[Body] = None
    date: Optional[DateUpdate] = None

    chassis: Optional[Chassis] = None
    generations: List[Generations] = Field(default_factory=list)
    manufacturer: Any = None
    transmission: Optional[Transmission] = None

    comment: Optional[str] = Field(None, alias="_comment")


#  __all__ = ["TechData"]  # cuz I don't want to export all types in tests
