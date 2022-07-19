from __future__ import annotations

import dataclasses
from types import TracebackType
from typing import List, Tuple, Type, Any, Dict, Optional, Union, cast, overload, Literal, Callable

from avtocod import AvtoCod
from avtocod.avtocod import PipelineT
from avtocod.exceptions import AvtocodException, PipelineException
from avtocod.methods import AvtocodMethod, AvtocodType, MultiRequest
from avtocod.utils.utils import is_pipeline_supported


class Pipeline:
    def __init__(self, *args, **kwargs):
        self._avtocod = _AvtoCodReturnMethod(*args, **kwargs)

        self._method_stack: List[PipelineMethod] = []

    async def __aenter__(self: PipelineT) -> PipelineT:
        return self

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[TracebackType],
    ) -> None:
        await self.reset()

    def __getattr__(self: PipelineT, item) -> PipelineT:
        avtocod_attr = getattr(self._avtocod, item, None)
        if not is_pipeline_supported(avtocod_attr):
            raise AttributeError(f"Cannot chain {item}!")

        self._method_stack.append(PipelineMethod(avtocod_attr))

        return self

    def __call__(self: PipelineT, *args, **kwargs) -> PipelineT:
        last_element = self._method_stack[-1]
        last_element.args = args
        last_element.kwargs = kwargs
        return self

    def __len__(self) -> int:
        return len(self._method_stack)

    def __bool__(self) -> bool:
        return True

    async def reset(self) -> None:
        self._method_stack = []

    async def _execute_transaction(
            self,
            methods: List[AvtocodMethod[AvtocodType]],
            raise_on_error: bool = False,
            request_timeout: Optional[int] = None,
    ) -> List[Union[AvtocodType, AvtocodException]]:

        try:
            responses = await self._avtocod.session(
                self._avtocod, MultiRequest(methods=methods), timeout=request_timeout
            )
        except PipelineException as e:
            if raise_on_error:
                errors = [r.result for r in e.results_and_error
                          if isinstance(r.result, AvtocodException)]
                raise errors[0] from e
            return [method_and_r_or_e.result for method_and_r_or_e in e.results_and_error]

        return cast(List[AvtocodType], responses)

    @overload
    async def execute(
            self,
            raise_on_error: Literal[True] = True,
            request_timeout: Optional[int] = None
    ) -> List[AvtocodType]:
        ...

    async def execute(
            self, raise_on_error: bool = True, request_timeout: Optional[int] = None
    ) -> List[Union[AvtocodType, AvtocodException]]:
        if not self._method_stack:
            raise AttributeError("No method to execute!")

        methods = []
        for method in self._method_stack:
            if not method.method_callable:
                raise AttributeError("You must call a method before calling execute!")
            if all([arg is None for arg in (method.args, method.kwargs)]):
                raise AttributeError("You must call a method with args or kwargs before calling execute!")

            methods.append(
                method.method_callable(
                    *method.args,
                    **method.kwargs
                )
            )

        return await self._execute_transaction(methods, raise_on_error, request_timeout)


@dataclasses.dataclass
class PipelineMethod:
    method_callable: Optional[Callable[..., AvtocodMethod[Any]]] = None
    args: Optional[Tuple[Any, ...]] = dataclasses.field(default_factory=tuple)
    kwargs: Optional[Dict[str, Any]] = dataclasses.field(default_factory=dict)


class _AvtoCodReturnMethod(AvtoCod):
    def __call__(  # type: ignore[override]
            self,
            method: AvtocodMethod[AvtocodType],
            request_timeout: Optional[int] = None,
    ) -> AvtocodMethod[AvtocodType]:
        return method
