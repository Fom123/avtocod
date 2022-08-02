from __future__ import annotations

from types import TracebackType
from typing import Any, List, Optional, Type, Union, Awaitable, TypeVar, Callable

from avtocod import AvtoCod
from avtocod.avtocod import PipelineT
from avtocod.exceptions import AvtocodException, PipelineException
from avtocod.methods import AvtocodMethod, AvtocodType, MultiRequest
from avtocod.utils.utils import is_pipeline_supported

F = TypeVar("F", bound=Callable[..., Any])


class Pipeline:
    def __init__(self, avtocod: AvtoCod) -> None:
        self.avtocod = avtocod
        self.method_stack: List[AvtocodMethod[Any]] = []

    async def __aenter__(self: PipelineT) -> PipelineT:
        return self

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[TracebackType],
    ) -> None:
        self.reset()

    def __getattr__(self: PipelineT, item: str) -> Any:
        """We are overriding call on avtocod to get a method and push it to the stack"""

        def push_to_stack(
                method: AvtocodMethod[AvtocodType],
                request_timeout: Optional[int] = None,
        ) -> None:
            self.method_stack.append(method)

        def wrapper(
                *args: Any,
                **kwargs: Any
        ) -> PipelineT:
            function_that_call_avtocod = getattr(AvtoCod, item)  # get the function from avtocod
            if not is_pipeline_supported(function_that_call_avtocod):
                raise AttributeError(f"{item} is not supported in pipeline")

            # call the function from avtocod with the args and kwargs and our custom push_to_stack function
            function_that_call_avtocod(push_to_stack, *args, **kwargs)

            return self

        return wrapper

    def __len__(self) -> int:
        return len(self.method_stack)

    def __bool__(self) -> bool:
        return True

    def reset(self) -> None:
        self.method_stack = []

    async def _execute_transaction(
            self,
            methods: List[AvtocodMethod[AvtocodType]],
            raise_on_error: bool = False,
            request_timeout: Optional[int] = None,
    ) -> List[Union[AvtocodType, AvtocodException]]:

        try:
            responses = await self.avtocod(
                method=MultiRequest(methods=methods), request_timeout=request_timeout
            )
        except PipelineException as e:
            if raise_on_error:
                errors = [
                    r.result for r in e.results_and_error if isinstance(r.result, AvtocodException)
                ]
                raise errors[0] from e
            return [method_and_r_or_e.result for method_and_r_or_e in e.results_and_error]

        return responses  # type: ignore

    def execute(
            self, raise_on_error: bool = True, request_timeout: Optional[int] = None
    ) -> Awaitable[List[Union[AvtocodType, AvtocodException]]]:
        if not self.method_stack:
            raise AttributeError("No method to execute!")

        try:
            return self._execute_transaction(
                self.method_stack,
                raise_on_error,
                request_timeout
            )
        finally:
            self.reset()
