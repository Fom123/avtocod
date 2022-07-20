from typing import Any, List, Optional

from pydantic import Field

from avtocod.types import AvtocodObject


class GotsAuctions(AvtocodObject):
    items: Optional[List[Any]] = None
    comment: Optional[str] = Field(None, alias="_comment")
    date: Optional[Any] = None
