from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Awaitable, Callable, Union

from ...methods import AvtocodMethod, AvtocodType
from ...methods.base import ResponseType

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
