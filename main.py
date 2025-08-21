import asyncio
import json

from src.utils.logger import logger
from src.services import OLXService, ShafaService
from src.clients.api import OLXClient, ShafaClient


async def main() -> None:
    olx_service = OLXService(
        olx_client=OLXClient()
    )
    shafa_service = ShafaService(
        shafa_client=ShafaClient()
    )
    olx_data = await olx_service.get_products(query="кросівки", filter_float_price_from=10000, filter_state_enum="used", filter_float_size_from="35")
    with open("olx_data.json", "w", encoding="utf-8") as file:
        json.dump(olx_data, file, ensure_ascii=False, indent=4)
    shafa_data_all = await shafa_service.get_products_all(search_text="кросівки", price_from=50, price_to=100)
    shafa_data_top = await shafa_service.get_products_top(search_text="кросівки", price_from=50, price_to=100)
    with open("shafa_all.json", "w", encoding="utf-8") as file:
        json.dump(shafa_data_all, file, ensure_ascii=False, indent=4)
    with open("shafa_top.json", "w", encoding="utf-8") as file:
        json.dump(shafa_data_top, file, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    asyncio.run(main())
