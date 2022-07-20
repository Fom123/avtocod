import pytest

from avtocod.methods import GetToken
from avtocod.types import Token
from tests.mocked_api import MockedAvtoCod

pytestmark = pytest.mark.asyncio


class TestGetToken:
    async def test_method(self, avtocod: MockedAvtoCod) -> None:
        prepare_result = avtocod.add_result_for(  # type: ignore
            GetToken,
            result=Token(token="token"),
        )

        response = await GetToken()
        request = avtocod.get_request()

        assert isinstance(request.data, dict)
        assert request.data["method"] == "token.get"
        assert request.data["params"] == {}
        assert prepare_result.result
        assert response == prepare_result.result.token  # it should return str, not the Token

    async def test_avtocod_method(self, avtocod: MockedAvtoCod) -> None:
        prepare_result = avtocod.add_result_for(  # type: ignore
            GetToken,
            result=Token(token="token"),
        )

        response = await avtocod.get_token()
        request = avtocod.get_request()

        assert isinstance(request.data, dict)
        assert request.data["method"] == "token.get"
        assert request.data["params"] == {}

        assert prepare_result.result
        assert response == prepare_result.result.token
