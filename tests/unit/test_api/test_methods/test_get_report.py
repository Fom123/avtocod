import pytest

from avtocod.methods import GetReport
from avtocod.types import Report
from tests.mocked_api import MockedAvtoCod

pytestmark = pytest.mark.asyncio


class TestGetReport:
    async def test_method(self, avtocod: MockedAvtoCod, report: Report) -> None:
        prepare_result = avtocod.add_result_for(
            GetReport,
            result=report,
        )

        response = await GetReport(uuid=report.uuid)
        request = avtocod.get_request()

        assert isinstance(request.data, dict)
        assert request.data["method"] == "report.get"
        assert request.data["params"] == {"uuid": report.uuid}
        assert response == prepare_result.result

    async def test_avtocod_method(self, avtocod: MockedAvtoCod, report: Report) -> None:
        prepare_result = avtocod.add_result_for(
            GetReport,
            result=report,
        )

        response = await avtocod.get_report(report.uuid)
        request = avtocod.get_request()

        assert isinstance(request.data, dict)
        assert request.data["method"] == "report.get"
        assert request.data["params"] == {"uuid": report.uuid}
        assert response == prepare_result.result



