import asyncio
import json

from src.utils.logger import logger
from src.services import OLXService
from src.clients.api import OLXClient


async def main() -> None:
    service = OLXService(
        olx_client=OLXClient()
    )
    data = await service.get_products(query="кросівки")
    # logger.info(f"PRODUCTS: {data}")
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    asyncio.run(main())
