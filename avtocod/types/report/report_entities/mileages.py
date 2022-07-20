from typing import Any, Dict, List, Optional

from pydantic import Field

from avtocod.types import AvtocodObject
from avtocod.types.reusable import CountItems


class Actuality(AvtocodObject):
    date: Optional[str] = None


class FilledBy(AvtocodObject):
    source: Optional[str] = None


class Item(AvtocodObject):
    id: Optional[int] = Field(None, alias="_id")
    mileage: Optional[int] = None
    actuality: Optional[Actuality] = None
    filled_by: Optional[FilledBy] = None
    date: Optional[Dict[str, Any]] = None


class Mileages(CountItems):
    items: List[Item] = Field(default_factory=list)
