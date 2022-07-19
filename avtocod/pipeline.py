from __future__ import annotations

from types import TracebackType
from typing import List, Tuple, Type, Any, Dict, Optional, Union, cast, overload, Literal, Callable

from avtocod import AvtoCod
from avtocod.avtocod import PipelineT
from avtocod.exceptions import AvtocodException, PipelineException
from avtocod.methods import AvtocodMethod, AvtocodType, MultiRequest
from avtocod.utils.utils import is_pipeline_supported


class Pipeline:
    def __init__(self, *args, **kwargs):
        self._avtocod_args = args
        self._avtocod_kwargs = kwargs
        self._avtocod = _AvtoCodReturnMethod(*args, **kwargs)

        self._previous: Optional[Pipeline] = None
        self._method_callable: Optional[Callable[..., AvtocodMethod[Any]]] = None
        self._method_args: Optional[Tuple[...]] = None
        self._method_kwargs: Optional[Dict[str, Any]] = None

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

        self._method_callable = avtocod_attr

        return self

    def __call__(self: PipelineT, *args, **kwargs) -> PipelineT:
        self._method_args = args
        self._method_kwargs = kwargs

        pipeline = type(self)(*self._avtocod_args, **self._avtocod_kwargs)
        pipeline._previous = self

        return pipeline

    def __len__(self) -> int:
        return len(self.method_stack)

    def __bool__(self) -> bool:
        return True

    async def reset(self) -> None:
        self._previous = None
        self._method_callable = None
        self._method_args = None
        self._method_kwargs = None

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
                raise e.results_and_error[0][1]
            return [method_and_r_or_e[1] for method_and_r_or_e in e.results_and_error]

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
        if not self._previous:
            raise AttributeError("No method to execute!")

        methods = []
        pipeline = self._previous
        while pipeline is not None:
            if not pipeline._method_callable:
                raise AttributeError("You must call a method before calling execute!")
            if not (pipeline._method_args or pipeline._method_kwargs):
                raise AttributeError("You must call a method with args or kwargs before calling execute!")

            methods.append(
                pipeline._method_callable(*pipeline._method_args, **pipeline._method_kwargs)
            )
            pipeline = pipeline._previous

        methods.reverse()

        return await self._execute_transaction(methods, raise_on_error, request_timeout)


class _AvtoCodReturnMethod(AvtoCod):
    def __call__(  # type: ignore[override]
            self,
            method: AvtocodMethod[AvtocodType],
            request_timeout: Optional[int] = None,
    ) -> AvtocodMethod[AvtocodType]:
        return method
