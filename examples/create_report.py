import asyncio
import logging

from avtocod import AvtoCod
from avtocod.types import QueryNumber

EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )  # setup logging
    avtocod = await AvtoCod.from_credentials(EMAIL, PASSWORD)  # create instance of avtocod class

    report = await avtocod.create_report(
        "KNAFU611BA5295980", query_type=QueryNumber.VIN  # or just "VIN"
    )  # creating the report

    while True:
        report = await avtocod.get_report(report.uuid)  # getting report until it's ready
        if (
                report.is_ready or report.is_completed
        ):  # checking if report is ready or completed, if yes, exit the cycle
            break
        await asyncio.sleep(5)

    print(
        report.dict()
    )  # you can print the dict of your report now, cuz it's inheriting from pydantic BaseModel

    await avtocod.session.close()  # closing the session, so we won't have errors


if __name__ == "__main__":
    asyncio.run(main())
