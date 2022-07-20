from typing import Any

from avtocod.utils.generators import generate_next_id, generate_next_uuid


def generate_id(type_: str, /) -> Any:
    """
    Generate id
    Usage: id = generate_id()
    :return:
    """

    fabric = {"uuid": generate_next_uuid(), "natural": generate_next_id()}

    def wrapper() -> Any:
        choice = fabric[type_.casefold()]
        return next(choice)

    return wrapper
