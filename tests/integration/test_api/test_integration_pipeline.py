import asyncio
from typing import List, cast

import pytest

from avtocod import AvtoCod
from avtocod.types import Report
from avtocod.utils.utils import chunks
from tests.integration.conftest import uuids_

pytestmark = [pytest.mark.asyncio, pytest.mark.integration]


@pytest.mark.parametrize("uuids", chunks(uuids_(), 100))
async def test_integration_pipeline(uuids: str, real_avtocod: AvtoCod) -> None:
    async with real_avtocod.pipeline() as pipeline:
        for uuid in uuids:
            pipeline.get_report(uuid)
        responses = await pipeline.execute(raise_on_error=False)
        assert all(isinstance(response, Report) for response in responses)

        assert all(response.uuid for response in responses)
        assert all(response.avtocod is real_avtocod for response in responses)
        assert len(responses) == len(uuids)

        await asyncio.sleep(1)  # wait before getting the report again
