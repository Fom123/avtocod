from typing import Any, List, Dict, Union, Tuple

from avtocod.exceptions import AvtocodException, PipelineException
from avtocod.methods.base import AvtocodMethod, JsonrpcRequest, ResponseType, Data, Request, AvtocodType


class MultiRequest(AvtocodMethod[Any]):
    """Methods to be executed once at a time"""

    methods: List[AvtocodMethod[Any]]
    http_method: str = "POST"

    __returning__ = List[Any]

    def build_jsonrpc_request(self) -> JsonrpcRequest:
        """It's a batch request, so we have to build a batch request from the list of methods"""
        raise NotImplementedError

    def build_request(self) -> Request:
        return Request.from_batch_jsonrpc(
            [methods.build_jsonrpc_request() for methods in self.methods],
            http_method=self.http_method
        )

    def build_response(self, data: Data) -> ResponseType[Any]:
        assert isinstance(data, list), "data must be a list"

        if all(isinstance(data_["id"], int) for data_ in data):
            data = sorted(data, key=lambda x: x["id"])  # type: ignore

        method_data = zip(self.methods, data)

        methods_exceptions: List[
            Tuple[AvtocodMethod[Any], Union[AvtocodException, AvtocodType]]
        ] = []
        exception = False

        for k, v in method_data:
            try:
                methods_exceptions.append((k, k.build_response(v)))
            except AvtocodException as e:
                exception = True
                methods_exceptions.append((k, e))

        if exception:
            raise PipelineException(
                "Got errors when chaining methods", results_and_error=methods_exceptions
            )

        return [methods_exceptions[1] for methods_exceptions in methods_exceptions]
