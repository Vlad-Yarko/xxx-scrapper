from typing import Optional
    
from src.services.product import ProductService
from src.clients import ProductClient


class ShafaService(ProductService):
    def __init__(
        self,
        olx_client: ProductClient
        ):
        super().__init__(
            client=olx_client
        )

    async def get_products_all(self, *args, **kwargs) -> Optional[dict]:
        data = await self.client.get_products_all(*args, **kwargs)
        return data

    async def get_products_top(self, *args, **kwargs) -> Optional[dict]:
        data = await self.client.get_products_top(*args, **kwargs)
        return data

