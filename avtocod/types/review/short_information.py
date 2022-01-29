from typing import Optional

from pydantic import BaseModel, validator

BASE_AVTOCOD_REPORT_URI = "https://profi.avtocod.ru/report/"


class ShortInformation(BaseModel):
    car_time: Optional[str] = None
    title: Optional[str] = None
    gos_number: Optional[str] = None
    vin: Optional[str] = None
    query_type: Optional[str] = None
    uuid: Optional[str] = None
    photo: Optional[str] = None
    logotype: Optional[str] = None

    @property
    def link(self):
        return BASE_AVTOCOD_REPORT_URI + self.uuid

    @validator("gos_number", "vin")
    def upper(cls, v: str):
        return v.upper()


__all__ = ["ShortInformation"]
