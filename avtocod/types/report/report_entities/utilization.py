from typing import Optional

from avtocod.types.reusable import CountItems


class Utilizations(CountItems):
    was_utilized: Optional[bool] = None
