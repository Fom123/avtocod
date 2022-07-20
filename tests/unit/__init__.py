import uuid

import pytest

from avtocod.methods import AuthLogin
from avtocod.types import LoginData
from tests.mocked_api import MockedAvtoCod

pytestmark = pytest.mark.asyncio


class TestGetReport:
    async def test_method(self, avtocod: MockedAvtoCod) -> None:
        prepare_result = avtocod.add_result_for(
            AuthLogin,
            result=LoginData(
                uuid=str(uuid.uuid4()),
                token="jwt.token",
                email="some_email",
                phone="+7_777_777_00",
                first_name="Vladimir",
                last_name="Putin",
            ),
        )

        response = await AuthLogin(email="some_email", password="some_password")
        request = avtocod.get_request()
        assert request.data["method"] == "auth.login"
        assert response == prepare_result.result

    async def test_avtocod_method(self, avtocod: MockedAvtoCod) -> None:
        prepare_result = avtocod.add_result_for(
            AuthLogin,
            result=LoginData(
                uuid=str(uuid.uuid4()),
                token="jwt.token",
                email="some_email",
                phone="+7_777_777_00",
                first_name="Vladimir",
                last_name="Putin",
            ),
        )

        response = await avtocod.login(email="some_email", password="some_password")
        request = avtocod.get_request()

        assert request.data["method"] == "auth.login"
        assert response == prepare_result.result
