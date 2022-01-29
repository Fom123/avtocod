from typing import Optional

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
    _comment: Optional[str] = None


__all__ = ["Vehicle", "Identifiers"]
