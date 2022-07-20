from typing import Any, Optional

from pydantic import Field

from avtocod.types.base import AvtocodObject


class Vehicle(AvtocodObject):
    pts: Optional[str] = None
    sts: Optional[str] = None
    vin: Optional[str] = None
    body: Optional[str] = None
    chassis: Optional[str] = None
    reg_num: Optional[str] = None


class Identifiers(AvtocodObject):
    vehicle: Optional[Vehicle] = None
    manufacture: Any = Field(default_factory=list)
    comment: Optional[str] = Field(None, alias="_comment")
