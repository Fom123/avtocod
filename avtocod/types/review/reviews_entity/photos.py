from typing import Any, Optional, List

from pydantic import Field

from avtocod.types import AvtocodObject, DateUpdate
from avtocod.types.reusable import Issued


class PhotoItemVehicle(AvtocodObject):
    brand: Any = None
    model: Any = None


class PhotosItem(AvtocodObject):
    id: Optional[int] = Field(None, alias="_id")
    uri: Optional[str]
    date: Optional[Issued]
    vehicle: Optional[PhotoItemVehicle]


class Photos(AvtocodObject):
    date: Optional[DateUpdate] = None
    count: Optional[int] = None
    items: Optional[List[PhotosItem]] = None
    comment: Optional[str] = Field(None, alias="_comment")


class Images(AvtocodObject):
    photos: Optional[Photos] = None
    comment: Optional[str] = Field(None, alias="_comment")
