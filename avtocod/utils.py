import functools
from typing import Any, Dict, List, Optional, TypeVar, Union, overload

T = TypeVar("T")


@overload
def wrap_as_list(value: None) -> List[Any]:
    ...


@overload
def wrap_as_list(value: List[T]) -> List[T]:
    ...


@overload
def wrap_as_list(value: Union[List[T], T]) -> List[T]:
    ...


def wrap_as_list(value: Optional[T]) -> Union[List[T], List[Any]]:
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
