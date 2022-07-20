from datetime import datetime
from typing import Any, List, Optional

from pydantic import Field

from avtocod.types.base import AvtocodObject


class GenericDateTime(AvtocodObject):
    """"""


class DateUpdate(AvtocodObject):
    update: Optional[datetime] = Field(
        None, description="Дата обновления данных", examples=["2020-02-19 21:10:00"]
    )


class DateReceive(AvtocodObject):
    date: Optional[datetime] = Field(
        None, description="Дата получения данных", examples=["2020-02-19 21:10:00"]
    )


class DateEvent(AvtocodObject):
    event: Optional[datetime] = Field(
        None, description="Дата события", examples=["2020-02-19 21:10:00"]
    )


class DateDate(AvtocodObject):
    date: Optional[datetime] = None


class DateStartEnd(AvtocodObject):
    start: Optional[datetime] = Field(
        None, description="Дата начала", examples=["2020-02-19 21:10:00"]
    )
    end: Optional[datetime] = Field(
        None, description="Дата окончания", examples=["2020-02-19 21:10:00"]
    )


class StartEnd(AvtocodObject):
    end: Optional[int] = None
    start: Optional[int] = None


class DateEnd(AvtocodObject):
    end: Optional[datetime] = None


class DateEndPercent(AvtocodObject):
    date: Optional[DateEnd] = None
    percent: Optional[int] = None


class Name(AvtocodObject):
    name: Optional[str] = None


class Total(AvtocodObject):
    total: Optional[int] = None


class TypeA(AvtocodObject):
    type: Optional[str] = None


class Issued(AvtocodObject):
    issued: Optional[datetime] = None


class MaxMin(AvtocodObject):
    max: Optional[int] = None
    min: Optional[int] = None
    optimal: Optional[int] = None


class DatePublish(AvtocodObject):
    publish: Optional[datetime] = None


class AmountCurrencyPrice(AvtocodObject):
    amount: Optional[int] = None
    currency: Optional[str] = None


class Count(AvtocodObject):
    count: Optional[int] = None


class TypeAndTypeId(AvtocodObject):
    type: Optional[str] = None
    type_id: Optional[str] = None


class PositionAndPositionId(AvtocodObject):
    position: Optional[str] = None
    position_id: Optional[str] = None


class Value(AvtocodObject):
    value: Optional[str] = None


class Regions(AvtocodObject):
    yearly: Optional[Any] = None


class Current(AvtocodObject):
    city: Optional[Any] = None
    region: Optional[Any] = None
    yearly: Optional[Any] = None


class PriceWithRegion(AvtocodObject):
    moscow: Optional[Regions] = None
    current: Optional[Current] = None
    moscow_region: Optional[Regions] = None
    amount: Optional[int] = None
    currency: Optional[str] = None


class CountItems(AvtocodObject):
    count: Optional[int] = None
    items: Optional[List[Any]] = None
    comment: Optional[str] = Field(None, alias="_comment")
    date: Optional[DateUpdate] = None
