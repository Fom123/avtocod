import asyncio
import logging

from avtocod import AvtoCod
from avtocod.session.middlewares.request_logging import RequestLogging

REPORT_ID = "2245ff3c-70b6-41ba-986b-c43a6633a335"
REPORT_ID2 = "8b96d8f5-5f20-4681-a170-748725606d80"


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )  # setup logging
    logging.getLogger("avtocod.types.base").setLevel(logging.ERROR)

    avtocod = AvtoCod()

    avtocod.session.middleware(RequestLogging())

    async with avtocod.pipeline() as pipe:
        report1, report2, upgrade = await (
            pipe.get_report(REPORT_ID).get_report(REPORT_ID2).upgrade_report(REPORT_ID2)
        ).execute(raise_on_error=False)

    print(report1.information)
    print(report2.information)
    print(upgrade)

    await avtocod.session.close()  # closing the session, so we won't have errors


if __name__ == "__main__":
    asyncio.run(main())
