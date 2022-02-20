from typing import Any, Dict, List, Optional, Union, cast

from avtocod.methods.base import AvtocodMethod, AvtocodType, Request
from avtocod.types.review.reviews_list import Filters, Pagination, ReviewList, ReviewsList, Sort


class GetReviewsList(AvtocodMethod[List[ReviewsList]]):
    pagination: Optional[Pagination] = None
    sort: Optional[Sort] = None
    filters: Optional[Filters] = None

    __returning__ = ReviewList

    def build_request(self) -> Request:
        data: Dict[str, Any] = self.dict()
        return Request(method="reports.list", params=data)

    @classmethod
    def on_response_parse(cls, response: AvtocodType) -> Union[Any, AvtocodType]:
        return cast(List[ReviewsList], response.reports_list)
