from typing import Any, Dict, Optional

from avtocod.methods.base import AvtocodMethod, Request
from avtocod.types.review.reviews_list import Filters, Pagination, ReviewList, Sort


class GetReviewsList(AvtocodMethod[ReviewList]):
    pagination: Optional[Pagination] = None
    sort: Optional[Sort] = None
    filters: Optional[Filters] = None

    __returning__ = ReviewList

    def build_request(self) -> Request:
        data: Dict[str, Any] = self.dict()
        return Request(method="reports.list", params=data)
