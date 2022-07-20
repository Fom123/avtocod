from typing import Any, Dict

from avtocod.methods.base import AvtocodMethod, JsonrpcRequest
from avtocod.types.report.report import Report


class GetReport(AvtocodMethod[Report]):
    uuid: str

    __returning__ = Report

    def build_jsonrpc_request(self) -> JsonrpcRequest:
        data: Dict[str, Any] = self.dict()
        return JsonrpcRequest(method="report.get", params=data)
