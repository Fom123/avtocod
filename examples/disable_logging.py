import asyncio
import logging

from avtocod import AvtoCod

REPORT_ID = "2245ff3c-70b6-41ba-986b-c43a6633a335"


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )  # setup logging
    # set logging level to ERROR, so we won't log missing attributes
    logging.getLogger("avtocod").setLevel(logging.DEBUG)  # whole library
    # or only about the missing attributes
    # logging.getLogger("avtocod.types.base").setLevel(logging.ERROR)

    avtocod = AvtoCod()
    # you can create the instance without providing token and credentials,
    # but then you can use only get_report method and login method.

    report = await avtocod.get_report(REPORT_ID)
    print(
        f"""Short information about the report with ID - {REPORT_ID}:
Title: {report.information.title}
Vin number: {report.information.vin},
Gos number: {report.information.gos_number},
Time: {report.information.car_time},
Link: {report.information.link},
Photo: {" ".join(report.information.photos) if report.information.photos else None}
"""
    )

    await avtocod.session.close()  # closing the session, so we won't have errors


if __name__ == "__main__":
    asyncio.run(main())
