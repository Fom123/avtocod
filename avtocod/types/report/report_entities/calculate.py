from typing import Optional

from pydantic import Field

from avtocod.types import AvtocodObject
from avtocod.types.reusable import PriceWithRegion, Regions, Value


class Coefficients(AvtocodObject):
    regional: Optional[Value] = None


class Osago(AvtocodObject):
    price: Optional[PriceWithRegion] = None
    comment: Optional[str] = Field(None, alias="_comment")
    coefficients: Optional[Coefficients] = None


class Tax(AvtocodObject):
    moscow: Optional[Regions] = None
    regions: Optional[Regions] = None


class Calculate(AvtocodObject):
    tax: Optional[Tax] = None
    osago: Optional[Osago] = None
    comment: Optional[str] = Field(None, alias="_comment")
