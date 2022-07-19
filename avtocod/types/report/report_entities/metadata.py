from typing import Any, Dict, List, Optional

from pydantic import Field

from avtocod.types import AvtocodObject


class Application(AvtocodObject):
    uid: Optional[str] = None
    version: Optional[str] = None


class Metadata(AvtocodObject):
    comment: Optional[str] = Field(None, alias="_comment")
    application: Optional[Application] = None
    functions: Optional[List[Dict[str, Any]]] = None
