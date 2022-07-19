import asyncio
import logging

from avtocod import AvtoCod
from avtocod.session.middlewares.relogin import ReLoginMiddleware, LoginPasswordGetter
from avtocod.session.middlewares.request_logging import RequestLogging

EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"


# run two instance of this script to see how it works
async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )  # setup logging
    avtocod = await AvtoCod.from_credentials(EMAIL, PASSWORD)  # create instance of avtocod class

    avtocod.session.middleware(ReLoginMiddleware(
        LoginPasswordGetter(EMAIL, PASSWORD)
    ))
    avtocod.session.middleware(RequestLogging())

    while True:
        print(await avtocod.get_account_info())
        await asyncio.sleep(5)

        async with avtocod.pipeline() as pipe:
            pipe.get_report("SOME_REPORT_ID").get_account_info()
            print(await pipe.execute())


if __name__ == "__main__":
    asyncio.run(main())
