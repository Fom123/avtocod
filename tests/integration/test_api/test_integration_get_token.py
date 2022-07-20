import pytest

from avtocod import AvtoCod
from tests.settings import NOT_AUTHORIZED

pytestmark = [pytest.mark.asyncio, pytest.mark.integration]


@pytest.mark.skipif(NOT_AUTHORIZED, reason="Not authorized")
async def test_integration_get_token(real_avtocod: AvtoCod) -> None:
    token = await real_avtocod.get_token()
    assert token is not None
    assert isinstance(token, str)
