import pytest

from avtocod.methods import AdditionalUpgrade
from avtocod.types import ReviewUpgrade, Report
from tests.mocked_api import MockedAvtoCod

pytestmark = pytest.mark.asyncio


class TestOrderRepair:
    async def test_method(self, avtocod: MockedAvtoCod, report: Report) -> None:
        prepare_result = avtocod.add_result_for(
            AdditionalUpgrade,
            ReviewUpgrade(channel="avtocod", max_wait_to_ready_time=60),
        )

        response = await AdditionalUpgrade(product_uuid="uuid", report_uuid=report.uuid)

        request = avtocod.get_request()

        assert isinstance(request.data, dict)
        assert request.data["method"] == "report.additional.upgrade"
        assert request.data["params"] == {"product_uuid": "uuid", "report_uuid": report.uuid}

        assert response == prepare_result.result

    async def test_avtocod_method(self, avtocod: MockedAvtoCod, report: Report) -> None:
        prepare_result = avtocod.add_result_for(
            AdditionalUpgrade,
            ReviewUpgrade(channel="avtocod", max_wait_to_ready_time=60),
        )

        response = await avtocod.upgrade_review_repair(uuid=report.uuid, product_uuid="uuid")

        request = avtocod.get_request()

        assert isinstance(request.data, dict)
        assert request.data["method"] == "report.additional.upgrade"
        assert request.data["params"] == {"product_uuid": "uuid", "report_uuid": report.uuid}
        assert response == prepare_result.result
