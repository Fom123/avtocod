from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Awaitable, Callable, Union

from ...methods import AvtocodMethod, AvtocodType, Response
from ...methods.base import ResponseType
from ...types import AvtocodObject

if TYPE_CHECKING:
    from ...avtocod import AvtoCod

NextRequestMiddlewareType = Callable[
    ["AvtoCod", AvtocodMethod[AvtocodType]], Awaitable[ResponseType[AvtocodType]]
]

RequestMiddlewareType = Union[
    "BaseRequestMiddleware",
    Callable[
        [NextRequestMiddlewareType[AvtocodType], "AvtoCod", AvtocodMethod[AvtocodType]],
        Awaitable[ResponseType[AvtocodType]],
    ],
]


class BaseRequestMiddleware(ABC):
    @abstractmethod
    async def __call__(
        self,
        make_request: NextRequestMiddlewareType[AvtocodType],
        avtocod: "AvtoCod",
        method: AvtocodMethod[AvtocodType],
    ) -> ResponseType[AvtocodType]:
        pass
