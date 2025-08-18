from src.utils.client import JSONClient
from src.enums.olx import URLEnum


class OLXClient(JSONClient):
    def __init__(self):
        super().__init__(
            base_url=URLEnum.BASE_URL.value
        )

    async def get_products(
        self,
        query: str,
        offset: int = 0,
        limit: int = 40
    ):
        self.endpoint = URLEnum.PRODUCTS_ENDPOINT_URL.value
        self.params = {
            "query": query,
            "offset": offset,
            "limit": limit
        }
        data = await self.get()
        return data
