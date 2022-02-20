from typing import Any, Dict, List, cast

from avtocod.methods.base import AvtocodMethod, AvtocodType


class MultiRequest(AvtocodMethod[Any]):
    """Order the additional car repair information"""

    methods: List[AvtocodMethod[Any]]
    count: int = 0
    __returning__ = List[Any]

    def build_request(self) -> Any:
        return [method.build_request() for method in self.methods]

    def build_response(self, data: Dict[str, Any]) -> AvtocodType:
        response = self.methods[self.count].build_response(data)
        self.count += 1
        return cast(AvtocodType, response)
