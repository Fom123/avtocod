from typing import Any, List, Optional

from pydantic import BaseModel

from avtocod.types.base import DateUpdate


class Name(BaseModel):
    original: Optional[str] = None
    normalized: Optional[str] = None


class Logotype(BaseModel):
    uri: Optional[str] = None


class ModelEngine(BaseModel):
    name: Optional[str] = None


class Standarts(BaseModel):
    emission: Optional[List[Any]] = None


class Chassis(BaseModel):
    number: Optional[str] = None
    _comment: Optional[str] = None


class Transmission(BaseModel):
    _comment: Optional[str] = None


class Color(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None


class Body(BaseModel):
    color: Optional[Color] = None
    number: Optional[str] = None
    _comment: Optional[str] = None


class Drive(BaseModel):
    type: Optional[str] = None
    type_id: Optional[str] = None
    _comment: Optional[str] = None


class Model(BaseModel):
    id: Optional[str] = None
    name: Optional[Name] = None
    _comment: Optional[str] = None


class Brand(BaseModel):
    id: Optional[str] = None
    name: Optional[Name] = None
    logotype: Optional[Logotype] = None


class Type(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    type_id: Optional[str] = None
    _comment: Optional[str] = None


class Wheel(BaseModel):
    _comment: Optional[str] = None
    position: Optional[str] = None
    position_id: Optional[str] = None
    position_code: Optional[str] = None


class Fuel(BaseModel):
    type: Optional[str] = None
    type_id: Optional[str] = None


class Power(BaseModel):
    hp: Optional[int] = None
    kw: Optional[int] = None


class Engine(BaseModel):
    fuel: Optional[Fuel] = None
    power: Optional[Power] = None
    number: Optional[str] = None
    volume: Optional[int] = None
    model: Optional[ModelEngine] = None
    standarts: Optional[Standarts] = None

    _comment: Optional[str] = None


class Weight(BaseModel):
    max: Optional[int] = None
    netto: Optional[int] = None
    _comment: Optional[str] = None


class TechData(BaseModel):
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
    generations: Optional[List[Any]] = None
    manufacturer: Optional[List[Any]] = None
    transmission: Optional[Transmission] = None

    _comment: Optional[str] = None


__all__ = ["TechData"]
