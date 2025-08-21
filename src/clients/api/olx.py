from typing import Union, Optional

from src.utils.client import JSONClient
from src.clients.product import ProductClient
from src.enums.olx import URLEnum, StateEnum


class OLXClient(ProductClient, JSONClient):
    def __init__(self):
        super().__init__(
            base_url=URLEnum.BASE_URL.value
        )

    async def get_products(
        self,
        query: str,
        offset: int = 0,
        limit: int = 40,
        filter_float_price_from: Optional[str] = None,
        filter_float_price_to: Optional[str] = None,
        filter_state_enum: Optional[StateEnum] = None
    ) -> Union[None, dict, list]:
        self.endpoint = URLEnum.PRODUCTS_ENDPOINT_URL.value
        self.params = {
            "query": query,
            "offset": offset,
            "limit": limit
        }
        optional_params = {
            "filter_float_price:from": filter_float_price_from,
            "filter_float_price:to": filter_float_price_to,
            "filter_enum_state[0]": filter_state_enum
        }
        self.params.update({k: v for k, v in optional_params.items() if v is not None})
        data = await self.get()
        return data
