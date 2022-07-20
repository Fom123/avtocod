import asyncio
from pathlib import Path
from typing import List

import pytest

from avtocod import AvtoCod
from tests import settings


# https://github.com/pytest-dev/pytest-asyncio/issues/127
# https://peps.python.org/pep-0550/
# https://gist.github.com/linw1995/a50928ed90d5e8c8c1b9575d7d7fe70c
# we have to use a fixture that is not a coroutine to apply context variables, see links above
@pytest.fixture(autouse=True)
def apply_context(real_avtocod: AvtoCod) -> None:
    token = AvtoCod.set_current(real_avtocod)
    try:
        yield
    finally:
        AvtoCod.reset_current(token)


@pytest.fixture(scope="session")
async def real_avtocod() -> AvtoCod:
    if settings.AVTOCOD_EMAIL and settings.AVTOCOD_PASSWORD:
        avtocod = await AvtoCod.from_credentials(
            settings.AVTOCOD_EMAIL, settings.AVTOCOD_PASSWORD
        )
    elif settings.AVTOCOD_TOKEN:
        avtocod = AvtoCod(settings.AVTOCOD_TOKEN)
    else:
        avtocod = AvtoCod()

    try:
        yield avtocod
    finally:
        await avtocod.session.close()


# The event_loop fixture can be overridden in any of the standard pytest locations, e.g. directly in the test file,
# or in conftest.py. https://pypi.org/project/pytest-asyncio/
@pytest.fixture(scope="session")
def event_loop() -> asyncio.AbstractEventLoop:
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


def uuids_() -> List[str]:
    path = Path(__file__).parent / "reports.txt"
    with path.open() as f:
        return [line.strip() for line in f]


uuids = pytest.fixture()(uuids_)
