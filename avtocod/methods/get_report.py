from typing import Any, Dict

from avtocod.methods.base import AvtocodMethod, Request
from avtocod.types.review.review import Review


class GetReport(AvtocodMethod[Review]):
    uuid: str

    __returning__ = Review

    def build_request(self) -> Request:
        data: Dict[str, Any] = self.dict()
        return Request(method="report.get", params=data)
