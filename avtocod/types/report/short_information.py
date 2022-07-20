import dataclasses
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from avtocod.types import QueryType

BASE_AVTOCOD_REPORT_URI = "https://profi.avtocod.ru/report/"


@dataclasses.dataclass
class ShortInformation:
    uuid: str
    car_time: str
    title: str
    query_type: "QueryType"
    gos_number: Optional[str] = None
    vin: Optional[str] = None
    photos: Optional[List[str]] = None
    logotype: Optional[str] = None

    @property
    def link(self) -> str:
        return BASE_AVTOCOD_REPORT_URI + self.uuid

    def __post_init__(self) -> None:
        if self.vin:
            self.vin.upper()
        if self.gos_number:
            self.gos_number.upper()


__all__ = ["ShortInformation"]
