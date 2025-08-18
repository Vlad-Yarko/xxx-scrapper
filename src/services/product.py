from typing import Optional

from src.utils.service import Service
from src.utils.client import client_session
from src.clients import ProductClient


class ProductService(Service):
    def __init__(
        self,
        client: ProductClient
    ):
        self.client = client

    @client_session
    async def get_products(self, *args, **kwargs) -> Optional[dict]:
        data = await self.client.get_products()
        if not data:
            return None
        return data
