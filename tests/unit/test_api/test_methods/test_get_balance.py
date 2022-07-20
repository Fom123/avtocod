import pytest

from avtocod.methods import GetBalance
from avtocod.types import Balance, BalanceItem
from tests.mocked_api import MockedAvtoCod

pytestmark = pytest.mark.asyncio


class TestGetBalance:
    async def test_method(self, avtocod: MockedAvtoCod) -> None:
        prepare_result = avtocod.add_result_for(  # type: ignore
            GetBalance, result=Balance(balance=[BalanceItem(product_uuid="uuid", count=5)])
        )

        response = await GetBalance()
        request = avtocod.get_request()

        assert isinstance(request.data, dict)
        assert request.data["method"] == "profile.balance"
        assert request.data["params"] == {}
        assert prepare_result.result
        assert response == prepare_result.result.balance

    async def test_avtocod_method(self, avtocod: MockedAvtoCod) -> None:
        prepare_result = avtocod.add_result_for(  # type: ignore
            GetBalance, result=Balance(balance=[BalanceItem(product_uuid="uuid", count=5)])
        )

        response = await avtocod.get_account_info()
        request = avtocod.get_request()

        assert isinstance(request.data, dict)
        assert request.data["method"] == "profile.balance"
        assert request.data["params"] == {}

        assert prepare_result.result
        assert response == prepare_result.result.balance
