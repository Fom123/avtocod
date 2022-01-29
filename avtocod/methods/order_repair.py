from typing import Any, Dict

from avtocod.methods.base import AvtocodMethod, Request
from avtocod.types.review.generation import ReviewUpgrade


class AdditionalUpgrade(AvtocodMethod[ReviewUpgrade]):
    """Order the additional car repair information"""

    report_uuid: str
    product_uuid: str

    __returning__ = ReviewUpgrade

    def build_request(self) -> Request:
        data: Dict[str, Any] = self.dict()

        return Request(method="report.additional.upgrade", params=data)
