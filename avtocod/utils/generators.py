from typing import Iterator
from uuid import uuid4


def generate_next_id(start: int = 1) -> Iterator[int]:
    """
    Generate next id
    Usage: for id in generate_next_id():
    :param start:
    :return:
    """
    while True:
        yield start
        start += 1


def generate_next_uuid() -> Iterator[str]:
    """
    Generate next uuid
    Usage: for uuid in generate_next_uuid():
    :return:
    """
    while True:
        yield str(uuid4())
