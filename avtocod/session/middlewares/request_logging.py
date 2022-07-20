import logging
from collections import defaultdict
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type

from ...methods import AvtocodMethod, AvtocodType
from ...methods.base import ResponseType
from .base import BaseRequestMiddleware, NextRequestMiddlewareType

if TYPE_CHECKING:
    from ...avtocod import AvtoCod

logger = logging.getLogger(__name__)


class RequestLogging(BaseRequestMiddleware):
    def __init__(self, ignore_methods: Optional[List[Type[AvtocodMethod[Any]]]] = None):
        """
        Middleware for logging outgoing requests
        :param ignore_methods: methods to ignore in logging middleware
        """
        self.ignore_methods = ignore_methods if ignore_methods else []
        self.counter: Dict[str, int] = defaultdict(int)

    async def __call__(
        self,
        make_request: NextRequestMiddlewareType[AvtocodType],
        avtocod: "AvtoCod",
        method: AvtocodMethod[AvtocodType],
    ) -> ResponseType[AvtocodType]:
        if type(method) not in self.ignore_methods:
            self.counter[str(method)] += 1
            logger.info(
                "Make request with method=%r (%d) by avtocod account with token = %r. "
                "Total Requests: %d",
                type(method).__name__,
                self.counter[str(method)],
                avtocod.token,
                sum(self.counter.values()),
            )
        return await make_request(avtocod, method)
