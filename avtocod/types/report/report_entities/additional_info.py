from typing import Any, Dict, List, Optional

from pydantic import Field

from avtocod.types import AvtocodObject
from avtocod.types.reusable import Name


class Category(AvtocodObject):
    code: Optional[str] = None
    description: Optional[str] = None


class GeoOwner(AvtocodObject):
    city: Optional[str] = None
    region: Optional[str] = None


class OwnerInfo(AvtocodObject):
    geo: Optional[GeoOwner] = None
    type: Optional[str] = None
    enforcement_proceedings: Any


class Segment(AvtocodObject):
    euro: Optional[List[Any]] = None


class DatePassport(AvtocodObject):
    receive: Optional[str] = None


class Passport(AvtocodObject):
    org: Optional[Name] = None
    date: Optional[DatePassport] = None
    number: Optional[str] = None
    has_dublicate: Optional[bool] = None


class Modifications(AvtocodObject):
    was_modificated: Optional[bool] = None


class VehicleInfo(AvtocodObject):
    notes: Optional[List[str]] = None
    owner: Optional[OwnerInfo] = None
    segment: Optional[Segment] = None
    category: Optional[Category] = None
    exported: Optional[bool] = None
    passport: Optional[Passport] = None
    modifications: Optional[Modifications] = None
    sts: Optional[Any] = None


class IdentifiersInfo(AvtocodObject):
    vin: Optional[Any] = None


class AdditionalInfo(AvtocodObject):
    vehicle: Optional[VehicleInfo] = None
    identifiers: Optional[IdentifiersInfo] = None
    comment: Optional[str] = Field(None, alias="_comment")
    catalog: Optional[Dict[str, Any]] = None  # TODO
