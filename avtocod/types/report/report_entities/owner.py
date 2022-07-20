from typing import Any, List, Optional

from pydantic import Field

from avtocod.types import AvtocodObject
from avtocod.types.reusable import DateStartEnd, DateUpdate


class OwnerHistory(AvtocodObject):
    type: Optional[str] = None
    company: Optional[Any] = None


class LastOperation(AvtocodObject):
    code: Optional[str] = None
    description: Optional[str] = None


class ItemHistory(AvtocodObject):
    id: Optional[int] = Field(None, alias="_id")
    date: Optional[DateStartEnd] = None
    owner: Optional[OwnerHistory] = None
    last_operation: Optional[LastOperation] = None


class HistoryOwnership(AvtocodObject):
    date: Optional[DateUpdate] = None
    count: Optional[int] = None
    items: Optional[List[ItemHistory]] = None
    comment: Optional[str] = Field(None, alias="_comment")


class Ownership(AvtocodObject):
    history: Optional[HistoryOwnership] = None
