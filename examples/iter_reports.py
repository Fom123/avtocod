import asyncio
import logging

from avtocod import AvtoCod

REPORT_ID = "2245ff3c-70b6-41ba-986b-c43a6633a335"
EMAIL, PASSWORD = "your_email", "your_password"


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )  # setup logging

    avtocod = await AvtoCod.from_credentials(email=EMAIL, password=PASSWORD)

    async for report in avtocod.iter_reports():
        print(report.uuid)

    await avtocod.session.close()  # closing the session, so we won't have errors


if __name__ == "__main__":
    asyncio.run(main())
