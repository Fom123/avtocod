from typing import Any, Dict

from avtocod.methods.base import AvtocodMethod, JsonrpcRequest
from avtocod.types.report.generation import ReviewUpgrade


class UpgradeReport(AvtocodMethod[ReviewUpgrade]):
    uuid: str

    __returning__ = ReviewUpgrade

    def build_jsonrpc_request(self) -> JsonrpcRequest:
        data: Dict[str, Any] = self.dict()

        return JsonrpcRequest(method="report.upgrade", params=data)
