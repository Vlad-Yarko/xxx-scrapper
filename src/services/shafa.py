from typing import Optional

from src.utils.client import client_session
from src.services.product import ProductService
from src.clients import ProductClient
from src.enums.shafa import StateEnum


class ShafaService(ProductService):
    def __init__(
        self,
        shafa_client: ProductClient
        ):
        super().__init__(
            client=shafa_client
        )

    @client_session
    async def get_products_all(
            self,
            search_text: str,
            page_enum: int = 1,
            first: int = 44,
            price_from: Optional[int] = None,
            price_to: Optional[int] = None,
            state: Optional[StateEnum] = None
        ) -> Optional[dict]:
        data = await self.client.get_products_all(
            search_text=search_text,
            page_enum=page_enum,
            first=first,
            price_from=price_from,
            price_to=price_to,
            state=state
        )
        return data

    @client_session
    async def get_products_top(
            self,
            search_text: str,
            page_enum: int = 1,
            first: int = 8,
            price_from: Optional[int] = None,
            price_to: Optional[int] = None,
            state: Optional[StateEnum] = None
        ) -> Optional[dict]:
        data = await self.client.get_products_top(
            search_text=search_text,
            page_enum=page_enum,
            first=first,
            price_from=price_from,
            price_to=price_to,
            state=state
        )
        return data
