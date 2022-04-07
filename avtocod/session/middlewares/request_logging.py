import logging
from collections import defaultdict
from typing import TYPE_CHECKING, Any, List, Optional, Type

from .base import BaseRequestMiddleware, NextRequestMiddlewareType
from ...methods import AvtocodMethod, Response
from ...types import AvtocodObject

if TYPE_CHECKING:
    from ...avtocod import Avtocod

logger = logging.getLogger(__name__)


class RequestLogging(BaseRequestMiddleware):
    def __init__(self, ignore_methods: Optional[List[Type[AvtocodMethod[Any]]]] = None):
        """
        Middleware for logging outgoing requests
        :param ignore_methods: methods to ignore in logging middleware
        """
        self.ignore_methods = ignore_methods if ignore_methods else []
        self.counter = defaultdict(int)

    async def __call__(
        self,
        make_request: NextRequestMiddlewareType,
        avtocod: "Avtocod",
        method: AvtocodMethod[AvtocodObject],
    ) -> Response[AvtocodObject]:
        if type(method) not in self.ignore_methods:
            self.counter[str(method)] += 1
            logger.info(
                "Make request with method=%r (%d) by avtocod account with token = %r. "
                "Total Requests: %d",
                type(method).__name__,
                self.counter[str(method)],
                avtocod.token,
                sum(self.counter.values())
            )
        return await make_request(avtocod, method)
