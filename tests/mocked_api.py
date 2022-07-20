from collections import deque
from itertools import zip_longest
from typing import TYPE_CHECKING, Deque, List, Optional, Tuple, Type, Any, Sequence

from avtocod import AvtoCod
from avtocod.exceptions import AvtocodException
from avtocod.methods import AvtocodError, AvtocodMethod, AvtocodType, JsonrpcRequest, Response
from avtocod.methods.base import Request
from avtocod.session.base import BaseSession, ResponseType
from avtocod.types import UNSET


class MockedSession(BaseSession):
    def __init__(self) -> None:
        super(MockedSession, self).__init__()
        self.responses: Deque[Response[Any]] = deque()
        self.requests: Deque[Request] = deque()
        self.closed = True

    def add_result(self, response: ResponseType[AvtocodType]) -> ResponseType[AvtocodType]:
        self.responses.append(response)
        return response

    def get_request(self) -> Request:
        return self.requests.pop()

    async def close(self) -> None:
        self.closed = True

    async def make_request(
            self, avtocod: AvtoCod, method: AvtocodMethod[AvtocodType], timeout: Optional[int] = UNSET
    ) -> ResponseType[AvtocodType]:
        self.closed = False
        self.requests.append(method.build_request())
        response: ResponseType[AvtocodType] = self.responses.pop()

        data = self.check_response(
            method=method,
            content_type="application/json",
            content=self.json_dumps(
                response.dict() if not isinstance(response, list)
                else [response_.dict() for response_ in response],
                default=str,
            )
        )
        return data


class MockedAvtoCod(AvtoCod):
    if TYPE_CHECKING:
        session: MockedSession

    def __init__(self, **kwargs: Any) -> None:
        super(MockedAvtoCod, self).__init__(
            kwargs.pop("token", "eyJ0e.abc"), session=MockedSession()
        )

    def add_result_for(
            self,
            method: Type[AvtocodMethod[AvtocodType]],
            result: Optional[AvtocodType] = None,
            error: Optional[AvtocodError] = None,
            jsonrpc: str = "2.0",
            id_: str = "",
    ) -> Response[AvtocodType]:
        response = Response[method.__returning__](  # type: ignore
            jsonrpc=jsonrpc, result=result, error=error, id=id_
        )
        self.session.add_result(response)
        return response

    def add_batch_result_for(
            self,
            methods: Sequence[Type[AvtocodMethod[AvtocodType]]],
            results: Sequence[AvtocodType],
            errors: Sequence[AvtocodError] = (),
            jsonrpcs: Sequence[str] = (),
            ids: Sequence[str] = ()
    ) -> List[Response[List[AvtocodType]]]:
        responses = []
        for method, result, error, jsonrpc, id_ in zip_longest(
                methods, results, errors, jsonrpcs, ids, fillvalue=None
        ):
            if jsonrpc is None:
                jsonrpc = "2.0"
            if id_ is None:
                id_ = ""
            response = Response[method.__returning__](  # type: ignore
                jsonrpc=jsonrpc, result=result, error=error, id=id_
            )
            responses.append(response)
        self.session.add_result(responses)
        return responses

    def get_request(self) -> Request:
        return self.session.get_request()
