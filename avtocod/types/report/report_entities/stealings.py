from typing import Optional

from avtocod.types.reusable import CountItems, DateUpdate


class Stealings(CountItems):
    date: Optional[DateUpdate] = None
    is_wanted: Optional[bool] = None
