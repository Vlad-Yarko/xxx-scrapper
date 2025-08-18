import asyncio

from src.utils.logger import logger
from src.services import OLXService
from src.clients.api import OLXClient


async def main() -> None:
    service = OLXService(
        olx_client=OLXClient()
    )
    data = await service.get_products()
    logger.info(f"PRODUCTS: {data}")


if __name__ == "__main__":
    asyncio.run(main())
