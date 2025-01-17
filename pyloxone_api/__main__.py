"""
A quick test of the pyloxone_api module

From the command line, run:

> python -m pyloxone_api username password host port

where username, password host and port are your Loxone login credentials

"""
import asyncio
import logging
import sys

from . import LoxAPI

_LOGGER = logging.getLogger("pyloxone_api")
_LOGGER.setLevel(logging.DEBUG)
_LOGGER.addHandler(logging.StreamHandler())


async def main():

    api = LoxAPI(
        user=sys.argv[1], password=sys.argv[2], host=sys.argv[3], port=sys.argv[4]
    )

    await api.getJson()
    await api.async_init()
    await api.start()

    return


if __name__ == "__main__":
    try:
        r = asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit()
