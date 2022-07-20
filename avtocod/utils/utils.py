import functools
from typing import Any, Callable, Dict, Final, Iterable, List, Optional, TypeVar, Union, overload

T = TypeVar("T")
F = TypeVar("F", bound=Callable[..., Any])
PIPELINE_IS_SUPPORTED: Final[str] = "pipeline_support"


def pipeline_support(f: F) -> F:
    setattr(f, PIPELINE_IS_SUPPORTED, True)
    return f


def is_pipeline_supported(f: Callable[..., Any]) -> bool:
    return getattr(f, PIPELINE_IS_SUPPORTED, False)


@overload
def wrap_as_list(value: None) -> List[Any]:
    ...


@overload
def wrap_as_list(value: List[T]) -> List[T]:
    ...


@overload
def wrap_as_list(value: Union[List[T], T]) -> List[T]:
    ...


def wrap_as_list(value: Any) -> Any:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def rgetattr(obj: Any, attr: str, *, default: Any = None) -> Any:
    def _getattr(obj: Any, attr: Any) -> Any:
        return getattr(obj, attr, default)

    return functools.reduce(_getattr, [obj] + attr.split("."))


def filter_payload(exclude: Optional[List[str]] = None, **kwargs: Any) -> Dict[Any, Any]:
    """
    Generate payload
    Usage: payload = generate_payload(**locals(), exclude=['foo'])
    :param exclude:
    :param kwargs:
    :return: dict
    """
    if exclude is None:
        exclude = []

    dictionary = {}
    for key, value in kwargs.items():
        if (
            key not in exclude + ["self", "cls", "kwargs", "args"]
            and value is not None
            and not key.startswith("_")
        ):
            dictionary[key] = value

    return dictionary


def chunks(list_: List[T], n: int) -> Iterable[List[T]]:
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(list_), n):
        yield list_[i : i + n]
