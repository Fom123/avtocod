import dataclasses
from typing import Any, Generic, List, Union

from avtocod.exceptions import AvtocodException, PipelineException
from avtocod.methods.base import (
    AvtocodMethod,
    AvtocodType,
    Data,
    JsonrpcRequest,
    Request,
    ResponseType,
)


@dataclasses.dataclass
class ResultOfBatch(Generic[AvtocodType]):
    avtocod_method: AvtocodMethod[AvtocodType]
    result: Union[AvtocodType, AvtocodException]


class MultiRequest(AvtocodMethod[Any]):
    """Methods to be executed once at a time"""

    methods: List[AvtocodMethod[Any]]

    __returning__ = List[Any]

    def build_jsonrpc_request(self) -> JsonrpcRequest:
        """It's a batch request, so we have to build a batch request from the list of methods"""
        raise NotImplementedError

    def build_request(self) -> Request:
        return Request.from_jsonrpc(
            [methods.build_jsonrpc_request() for methods in self.methods],
            http_method=self.http_method,
        )

    def build_response(self, data: Data) -> ResponseType[Any]:
        assert isinstance(data, list), "data must be a list"

        if all(isinstance(data_["id"], int) for data_ in data):
            data = sorted(data, key=lambda x: x["id"])  # type: ignore

        method_data = zip(self.methods, data)

        methods_exceptions: List[ResultOfBatch[Any]] = []
        exception = False

        for k, v in method_data:
            try:
                methods_exceptions.append(ResultOfBatch(k, k.build_response(v)))
            except AvtocodException as e:
                exception = True
                methods_exceptions.append(ResultOfBatch(k, e))

        if exception:
            raise PipelineException(
                "Got errors when chaining methods", results_and_error=methods_exceptions
            )

        return [methods_result.result for methods_result in methods_exceptions]
