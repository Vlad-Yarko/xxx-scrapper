from typing import Optional

from src.services.product import ProductService
from src.clients import ProductClient
from src.enums.olx import StateEnum


class OLXService(ProductService):
    def __init__(
        self,
        olx_client: ProductClient
        ):
        super().__init__(
            client=olx_client
        )

    async def get_products(
            self,
            query: str,
            offset: int = 0,
            limit: int = 40,
            filter_float_price_from: Optional[int] = None,
            filter_float_price_to: Optional[int] = None,
            filter_state_enum: Optional[StateEnum] = None,
            filter_float_size_from: Optional[str] = None,
            filter_float_size_to: Optional[str] = None
        ) -> dict | None:
        data =  await super().get_products(
            query=query,
            offset=offset,
            limit=limit,
            filter_float_price_from=filter_float_price_from,
            filter_float_price_to=filter_float_price_to,
            filter_state_enum=filter_state_enum,
            filter_float_size_from=filter_float_size_from,
            filter_float_size_to=filter_float_size_to
        )
        return data
