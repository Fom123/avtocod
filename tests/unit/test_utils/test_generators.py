from uuid import UUID

import pytest

from avtocod.utils import generate_id, generate_next_id, generate_next_uuid


def test_natural_iterator() -> None:
    natural_iterator = generate_next_id()

    assert next(natural_iterator) == 1
    assert next(natural_iterator) == 2
    assert next(natural_iterator) == 3


def test_uuid_iterator() -> None:
    uuid_iterator = generate_next_uuid()

    # Raise ValueError if badly formed hexadecimal UUID string
    UUID(next(uuid_iterator), version=4)


@pytest.mark.parametrize("name", ["natural", "Natural", "NaTurAl"])
def test_natural_fabric_generator(name: str) -> None:
    id_generator_func = generate_id(name)

    assert id_generator_func() == 1
    assert id_generator_func() == 2
    assert id_generator_func() == 3


@pytest.mark.parametrize("name", ["uuid", "UUID", "UuId"])
def test_uuid_fabric_generator(name: str) -> None:
    id_generator_func = generate_id(name)

    UUID(id_generator_func(), version=4)
