import asyncio
import logging

from avtocod import AvtoCod

EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    avtocod = await AvtoCod.from_credentials(EMAIL, PASSWORD)

    report = await avtocod.create_report("KNAFU611BA5295980", query_type="VIN")

    while True:
        report = await avtocod.get_report(report.uuid)
        if report.is_ready or report.is_completed:
            break
        await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
