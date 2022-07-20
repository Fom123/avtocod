from typing import Any, Dict

from pydantic import validator

from avtocod.methods.base import AvtocodMethod, JsonrpcRequest
from avtocod.types.report.generation import ReviewGeneration


class CreateReport(AvtocodMethod[ReviewGeneration]):
    __returning__ = ReviewGeneration

    query: str
    type: str

    @validator("type")
    def type_check(cls, v: str) -> str:
        v = v.upper()
        if v not in ["VIN", "GRZ", "BODY"]:
            raise TypeError("Incorrect type!")
        return v

    def build_jsonrpc_request(self) -> JsonrpcRequest:
        data: Dict[str, Any] = self.dict()
        return JsonrpcRequest(method="report.create", params=data)
