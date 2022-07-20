import asyncio
import logging

from avtocod import AvtoCod

EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )  # setup logging
    avtocod = await AvtoCod.from_credentials(EMAIL, PASSWORD)  # create instance of avtocod class

    created_report = await avtocod.create_report(
        "KNAFU611BA5295980", query_type="VIN"
    )  # creating the report
    await avtocod.upgrade_report(created_report.uuid)  # upgrading report_entities

    while True:
        report = await avtocod.get_report(
            created_report.uuid
        )  # getting the report until it's ready
        if (
            report.is_ready or report.is_completed
        ):  # checking if report is ready or completed, if yes, exit the cycle
            break
        await asyncio.sleep(5)

    print(report.information.link)  # now you can have the url of report

    await avtocod.session.close()  # closing the session, so we won't have errors


if __name__ == "__main__":
    asyncio.run(main())
