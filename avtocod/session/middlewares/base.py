from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Awaitable, Callable, Union

from ...methods import AvtocodMethod, AvtocodType, Response
from ...types import AvtocodObject

if TYPE_CHECKING:
    from ...avtocod import AvtoCod

NextRequestMiddlewareType = Callable[
    ["AvtoCod", AvtocodMethod[AvtocodObject]], Awaitable[Response[AvtocodObject]]
]

RequestMiddlewareType = Union[
    "BaseRequestMiddleware",
    Callable[
        [NextRequestMiddlewareType, "AvtoCod", AvtocodMethod[AvtocodType]],
        Awaitable[Response[AvtocodType]],
    ],
]


class BaseRequestMiddleware(ABC):
    @abstractmethod
    async def __call__(
        self,
        make_request: NextRequestMiddlewareType,
        avtocod: "AvtoCod",
        method: AvtocodMethod[AvtocodObject],
    ) -> Response[AvtocodObject]:
        pass
