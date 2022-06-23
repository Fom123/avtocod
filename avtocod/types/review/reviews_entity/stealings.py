from typing import Optional

from avtocod.types import DateUpdate
from avtocod.types.reusable import CountItems


class Stealings(CountItems):
    date: Optional[DateUpdate] = None
    is_wanted: Optional[bool] = None
