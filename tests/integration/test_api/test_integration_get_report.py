import pytest

from avtocod import AvtoCod
from avtocod.exceptions import NetworkError, ReportNotFound
from tests.integration.conftest import uuids_

pytestmark = [pytest.mark.asyncio, pytest.mark.integration]


@pytest.mark.parametrize("uuid", uuids_())
async def test_integration_get_report(real_avtocod: AvtoCod, uuid: str) -> None:
    try:
        report = await real_avtocod.get_report(uuid)
    except ReportNotFound:
        pytest.fail(f"Report with uuid {uuid} not found")
    except NetworkError:
        pytest.fail(f"Network error while getting report with uuid {uuid}")

    assert report.uuid == uuid
    assert report.avtocod is real_avtocod
