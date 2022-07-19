from typing import Any, Dict, List, Optional, Union, cast

from avtocod.methods.base import AvtocodMethod, AvtocodType, JsonrpcRequest
from avtocod.types.report.reports import BaseReport, Filters, Pagination, Reports, Sort


class GetReports(AvtocodMethod[List[BaseReport]]):
    pagination: Optional[Pagination] = None
    sort: Optional[Sort] = None
    filters: Optional[Filters] = None

    __returning__ = Reports

    def build_jsonrpc_request(self) -> JsonrpcRequest:
        data: Dict[str, Any] = self.dict()
        return JsonrpcRequest(method="reports.list", params=data)

    @classmethod
    def on_response_parse(cls, response: AvtocodType) -> Union[Any, AvtocodType]:
        return cast(List[BaseReport], response.reports_list)
