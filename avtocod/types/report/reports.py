from datetime import datetime, timedelta
from typing import Any, List, Optional, Union

from pydantic import Field, validator

from avtocod.types.base import AvtocodObject


class Filters(AvtocodObject):
    uuids: Optional[List[str]] = Field(None, examples=["21cf4dfb-2cd5-490a-9205-f3e9804bf0b0"])
    auto_index_from: Optional[int] = Field(None, examples=20)
    auto_index_to: Optional[int] = Field(None, examples=78)
    generation_date_from: Optional[Union[datetime, timedelta]] = Field(
        None, examples="2022-01-01T00:00:00+02:00"
    )
    generation_date_to: Optional[Union[datetime, timedelta]] = Field(
        None, examples="2022-01-01T00:00:00+02:00"
    )
    stages: Optional[List[str]] = Field(
        None, examples=["Норм отчет", "Осмотрена", "Куплена", "Посмотреть", "Покупать", "Шлак"]
    )
    tags_id: Optional[List[str]] = Field(
        None,
    )


class Sort(AvtocodObject):
    key: str
    order: str

    @validator("order")
    def order_validator(cls, v: str) -> str:
        if v not in ["desc", "asc"]:
            raise ValueError
        return v


class Pagination(AvtocodObject):
    page: int
    limit: int = Field(..., le=20)


class Query(AvtocodObject):
    type: str
    value: str


class BaseStatus(AvtocodObject):
    state: str
    block_status: str
    value: int


class BaseReport(AvtocodObject):
    uuid: str

    query: Optional[Query] = None
    brand_name_original: Optional[str] = None
    reg_num: Optional[str] = None
    year: Optional[int] = None
    vin: Optional[str] = None
    body: Optional[str] = None

    stage: str
    auto_index: int
    tags_ids: List[Any]
    additional_blocks: List[Any]
    is_ready: bool
    is_completed: bool

    accidents: Optional[BaseStatus] = None
    restrictions: Optional[BaseStatus] = None
    used_in_taxi: Optional[BaseStatus] = None
    stealings: Optional[BaseStatus] = None
    ownerships: Optional[BaseStatus] = None
    exploitations: Optional[BaseStatus] = None
    mileages: Optional[BaseStatus] = None
    repairs: Optional[BaseStatus] = None
    pledges: Optional[BaseStatus] = None

    max_wait_to_ready_time: Optional[int] = None
    generation_start_time: Optional[str] = None

    created_at: datetime
    updated_at: datetime


class Reports(AvtocodObject):
    pagination: Optional[Pagination] = None
    reports_list: List[BaseReport]


__all__ = ["Reports", "BaseReport", "BaseStatus", "Query", "Pagination", "Sort", "Filters"]
