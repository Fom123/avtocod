from typing import Any, Dict, Generator, List, Union

from avtocod.exceptions import AvtocodException
from avtocod.methods.base import AvtocodMethod, AvtocodType


class MultiRequest(AvtocodMethod[Any]):
    """Order the additional car repair information"""

    methods: List[AvtocodMethod[Any]]
    __returning__ = List[Any]

    def build_request(self) -> Any:
        return [method.build_request() for method in self.methods]

    def build_responses_from_generator(
        self, data_list: List[Dict[str, Any]]
    ) -> Generator[Union[AvtocodType, AvtocodException], None, None]:
        for method, data in zip(self.methods, data_list):
            try:
                yield method.build_response(data)
            except AvtocodException as e:
                yield e
