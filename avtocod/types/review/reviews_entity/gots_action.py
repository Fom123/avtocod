from typing import Optional, List, Any

from pydantic import Field

from avtocod.types import AvtocodObject


class GotsAuctions(AvtocodObject):
    items: Optional[List[Any]] = None
    comment: Optional[str] = Field(None, alias="_comment")
    date: Optional[List[Any]] = None
