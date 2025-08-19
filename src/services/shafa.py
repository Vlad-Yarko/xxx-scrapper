from typing import Optional

from src.utils.client import client_session
from src.services.product import ProductService
from src.clients import ProductClient


class ShafaService(ProductService):
    def __init__(
        self,
        shafa_client: ProductClient
        ):
        super().__init__(
            client=shafa_client
        )

    @client_session
    async def get_products_all(self, *args, **kwargs) -> Optional[dict]:
        data = await self.client.get_products_all(*args, **kwargs)
        return data

    @client_session
    async def get_products_top(self, *args, **kwargs) -> Optional[dict]:
        data = await self.client.get_products_top(*args, **kwargs)
        return data
