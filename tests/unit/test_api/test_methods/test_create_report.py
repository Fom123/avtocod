import pytest

from avtocod.methods import CreateReport
from avtocod.types import Report, ReviewGeneration
from tests.mocked_api import MockedAvtoCod

pytestmark = pytest.mark.asyncio


class TestCreateReport:
    async def test_method(self, avtocod: MockedAvtoCod, report: Report) -> None:
        prepare_result = avtocod.add_result_for(
            CreateReport,
            result=ReviewGeneration(uuid=report.uuid, channel="avtocod", max_generation_time=60),
        )

        response = await CreateReport(
            query=report.information.gos_number, type=report.information.query_type
        )
        request = avtocod.get_request()

        assert isinstance(request.data, dict)
        assert request.data["method"] == "report.create"
        assert request.data["params"] == {
            "query": report.information.gos_number,
            "type": report.information.query_type,
        }
        assert response == prepare_result.result

    async def test_avtocod_method(self, avtocod: MockedAvtoCod, report: Report) -> None:
        prepare_result = avtocod.add_result_for(
            CreateReport,
            result=ReviewGeneration(uuid=report.uuid, channel="avtocod", max_generation_time=60),
        )

        assert report.information.gos_number is not None

        response = await avtocod.create_report(
            query=report.information.gos_number, query_type=report.information.query_type
        )
        request = avtocod.get_request()

        assert isinstance(request.data, dict)
        assert request.data["method"] == "report.create"
        assert request.data["params"] == {
            "query": report.information.gos_number,
            "type": report.information.query_type,
        }

        assert response == prepare_result.result
