import pytest

from avtocod import AvtoCod
from avtocod.types import BalanceItem
from tests.settings import NOT_AUTHORIZED

pytestmark = [pytest.mark.asyncio, pytest.mark.integration]


@pytest.mark.skipif(NOT_AUTHORIZED, reason="Not authorized")
async def test_integration_get_account_info(real_avtocod: AvtoCod) -> None:
    account_info = await real_avtocod.get_account_info()
    assert all(isinstance(info, BalanceItem) for info in account_info)
    assert all(info.avtocod is real_avtocod for info in account_info)
    assert all(info.product_uuid is not None for info in account_info)
