import pytest

from avtocod import AvtoCod
from avtocod.types.report.reports import BaseReport
from tests.settings import NOT_AUTHORIZED

pytestmark = [
    pytest.mark.asyncio,
    pytest.mark.integration,
    pytest.mark.skipif(NOT_AUTHORIZED, reason="Not authorized"),
]


async def test_integration_get_reports(real_avtocod: AvtoCod) -> None:
    reports = await real_avtocod.get_reports()
    assert all(isinstance(report, BaseReport) for report in reports)
    assert all(report.avtocod is real_avtocod for report in reports)
    assert all(report.uuid is not None for report in reports)
    assert len(reports) > 0  # cuz we have at least one report


async def test_iter_reports(real_avtocod: AvtoCod) -> None:
    async for report in real_avtocod.iter_reports():
        assert isinstance(report, BaseReport)
        assert report.avtocod is real_avtocod
        assert report.uuid is not None
