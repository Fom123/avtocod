from typing import Any, List, Optional

from pydantic import Field

from avtocod.types import AvtocodObject
from avtocod.types.reusable import DateUpdate


class RegistrationActions:
    date: Optional[DateUpdate] = None
    count: Optional[int] = None
    items: List[Any] = Field(default_factory=list)
    comment: Optional[str] = Field(None, alias="_comment")
    has_restrictions: Optional[bool] = None


class RegistrationActionsArchive(AvtocodObject):
    date: Optional[DateUpdate] = None
    count: Optional[int] = None
    items: List[Any] = Field(default_factory=list)


class Restrictions(AvtocodObject):
    registration_actions: Optional[RegistrationActions] = None
