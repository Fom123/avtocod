from datetime import datetime
from typing import Optional

from avtocod.types import AvtocodObject


class LastGenerationStat(AvtocodObject):
    duration: Optional[int] = None
    start_time: Optional[datetime] = None
    complete_time: Optional[datetime] = None
