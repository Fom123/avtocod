from typing import Any, Dict

from avtocod.methods.base import AvtocodMethod, Request
from avtocod.types.review.generation import ReviewUpgrade


class UpgradeReport(AvtocodMethod[ReviewUpgrade]):
    uuid: str

    __returning__ = ReviewUpgrade

    def build_request(self) -> Request:
        data: Dict[str, Any] = self.dict()

        return Request(method="report.upgrade", params=data)
