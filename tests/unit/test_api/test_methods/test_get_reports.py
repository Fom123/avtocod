import datetime

import pytest

from avtocod.methods import GetReports
from avtocod.types.report.reports import BaseReport, Pagination, Reports
from tests.mocked_api import MockedAvtoCod

pytestmark = pytest.mark.asyncio


class TestGetReports:
    async def test_method(self, avtocod: MockedAvtoCod) -> None:
        prepare_result = avtocod.add_result_for(  # type: ignore
            GetReports,
            result=Reports(
                reports_list=[
                    BaseReport(
                        uuid="uuid",
                        stage="stage",
                        auto_index=44,
                        tags_ids=[],
                        additional_blocks=[],
                        is_ready=True,
                        is_completed=False,
                        created_at=datetime.datetime(2020, 1, 1, 0, 0, 0),
                        updated_at=datetime.datetime(2020, 1, 1, 0, 0, 0),
                    )
                ],
            ),
        )

        response = await GetReports(pagination=Pagination(page=1, limit=20))
        request = avtocod.get_request()

        assert isinstance(request.data, dict)
        assert request.data["method"] == "reports.list"
        assert request.data["params"] == {
            "pagination": {
                "page": 1,
                "limit": 20,
            },
            "filters": None,
            "sort": None,
        }
        assert prepare_result.result
        assert response == prepare_result.result.reports_list

    async def test_avtocod_method(self, avtocod: MockedAvtoCod) -> None:
        prepare_result = avtocod.add_result_for(  # type: ignore
            GetReports,
            result=Reports(
                reports_list=[
                    BaseReport(
                        uuid="uuid",
                        stage="stage",
                        auto_index=44,
                        tags_ids=[],
                        additional_blocks=[],
                        is_ready=True,
                        is_completed=False,
                        created_at=datetime.datetime(2020, 1, 1, 0, 0, 0),
                        updated_at=datetime.datetime(2020, 1, 1, 0, 0, 0),
                    )
                ],
            ),
        )

        response = await avtocod.get_reports(Pagination(page=1, limit=20))
        request = avtocod.get_request()

        assert isinstance(request.data, dict)
        assert request.data["method"] == "reports.list"
        assert request.data["params"] == {
            "pagination": {
                "page": 1,
                "limit": 20,
            },
            "filters": None,
            "sort": None,
        }  # all none will be stripped when sending the request
        assert prepare_result.result
        assert response == prepare_result.result.reports_list
