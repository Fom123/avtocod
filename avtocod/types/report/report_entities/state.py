from typing import List, Optional

from pydantic import Field

from avtocod.types import AvtocodObject


class Source(AvtocodObject):
    id: Optional[str] = Field(None, alias="_id")
    state: Optional[str] = None
    extended_state: Optional[str] = None


class State(AvtocodObject):
    sources: Optional[List[Source]]
