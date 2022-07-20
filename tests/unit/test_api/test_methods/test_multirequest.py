import pytest

from avtocod.methods import MultiRequest, GetReport, GetToken
from avtocod.types import Report, Token
from tests.mocked_api import MockedAvtoCod

pytestmark = [pytest.mark.asyncio]


class TestMultiRequest:
    async def test_method(
            self,
            avtocod: MockedAvtoCod,
            report: Report
    ) -> None:
        prepared_report_result, prepared_token_result = avtocod.add_batch_result_for(
            methods=(GetReport, GetToken),
            results=(report, Token(token="token")),
        )

        responses = await MultiRequest(
            methods=[
                GetReport(uuid=report.uuid),
                GetToken(),
            ],
        )
        request = avtocod.get_request()

        assert isinstance(request.data, list)

        request_report, request_token = request.data
        report_response, token_response = responses

        assert request_report["method"] == "report.get"
        assert request_report["params"] == {"uuid": report.uuid}

        assert request_token["method"] == "token.get"
        assert request_token["params"] == {}

        assert prepared_report_result.result
        assert prepared_report_result.result

        assert report_response == prepared_report_result.result
        assert token_response == prepared_token_result.result.token


    async def test_avtocod_method(
            self,
            avtocod: MockedAvtoCod,
            report: Report,
    ) -> None:
        prepared_report_result, prepared_token_result = avtocod.add_batch_result_for(
            methods=(GetReport, GetToken),
            results=(report, Token(token="token")),
        )

        async with avtocod.pipeline() as pipe:
            pipe.get_report(report.uuid)
            pipe.get_token()
            responses = await pipe.execute()

        request = avtocod.get_request()

        assert isinstance(request.data, list)

        request_report, request_token = request.data
        report_response, token_response = responses

        assert request_report["method"] == "report.get"
        assert request_report["params"] == {"uuid": report.uuid}

        assert request_token["method"] == "token.get"
        assert request_token["params"] == {}

        assert prepared_report_result.result
        assert prepared_report_result.result

        assert report_response == prepared_report_result.result
        assert token_response == prepared_token_result.result.token


