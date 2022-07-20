from typing import Any, List, Optional, Union

from pydantic import Field

from avtocod.types import AvtocodObject
from avtocod.types.report.report_entities.metadata import Metadata
from avtocod.types.report.report_entities.tech_data import Engine
from avtocod.types.reusable import (
    Count,
    DatePublish,
    DateUpdate,
    MaxMin,
    Name,
    PositionAndPositionId,
    PriceWithRegion,
    TypeA,
    TypeAndTypeId,
)


class GeoAd(AvtocodObject):
    city: Optional[str] = None
    street: Optional[str] = None
    country: Optional[str] = None


class VehicleAd(AvtocodObject):
    body: Optional[TypeAndTypeId] = None
    year: Optional[int] = None
    brand: Optional[Name] = None
    drive: Optional[TypeAndTypeId] = None
    model: Optional[Name] = None
    wheel: Optional[PositionAndPositionId] = None
    engine: Optional[Engine] = None
    owners: Optional[Union[Count, List[Any]]] = None
    condition: Optional[str] = None
    transmission: Optional[TypeAndTypeId] = None
    mileage: Optional[int] = None


class RelatedAd(AvtocodObject):
    geo: Optional[GeoAd] = None
    uri: Optional[str] = None
    date: Optional[DatePublish] = None
    price: Optional[PriceWithRegion] = None
    vehicle: Optional[VehicleAd] = None


class AdsItem(AvtocodObject):
    id: Optional[int] = Field(None, alias="_id")
    amount: Optional[MaxMin] = None
    mileage: Optional[int] = None
    currency: Optional[TypeA] = None
    metadata: Optional[Metadata] = None
    related_ads: List[RelatedAd] = Field(default_factory=list)


class Ads(AvtocodObject):
    date: Optional[DateUpdate] = None
    items: List[AdsItem] = Field(default_factory=list)
    comment: Optional[str] = Field(None, alias="_comment")


class MarketPrices(AvtocodObject):
    date: Optional[Any] = None
    items: Optional[List[Any]] = None
    comment: Optional[str] = Field(None, alias="_comment")
    ads: Optional[Ads] = None
