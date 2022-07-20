import pytest

from avtocod.methods import UpgradeReport
from avtocod.types import Report, ReviewUpgrade
from tests.mocked_api import MockedAvtoCod

pytestmark = pytest.mark.asyncio

class TestUpgradeReport:
    async def test_method(self, avtocod: MockedAvtoCod, report: Report) -> None:
        prepare_result = avtocod.add_result_for(
            UpgradeReport,
            result=ReviewUpgrade(channel="avtocod", max_wait_to_ready_time=60),
        )

        response = await UpgradeReport(uuid=report.uuid)
        request = avtocod.get_request()

        assert isinstance(request.data, dict)
        assert request.data["method"] == "report.upgrade"
        assert request.data["params"] == {"uuid": report.uuid}
        assert response == prepare_result.result

    async def test_avtocod_method(self, avtocod: MockedAvtoCod, report: Report) -> None:
        prepare_result = avtocod.add_result_for(
            UpgradeReport,
            result=ReviewUpgrade(channel="avtocod", max_wait_to_ready_time=60),
        )

        response = await avtocod.upgrade_report(uuid=report.uuid)
        request = avtocod.get_request()


        assert isinstance(request.data, dict)
        assert request.data["method"] == "report.upgrade"
        assert request.data["params"] == {"uuid": report.uuid}
        assert response == prepare_result.result