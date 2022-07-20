import pytest

from avtocod import AvtoCod
from tests.mocked_api import MockedAvtoCod


@pytest.fixture()
def avtocod() -> MockedAvtoCod:
    avtocod = MockedAvtoCod()
    token = AvtoCod.set_current(avtocod)
    try:
        yield avtocod
    finally:
        AvtoCod.reset_current(token)
