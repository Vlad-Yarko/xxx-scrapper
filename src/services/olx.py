from src.services.product import ProductService
from src.clients import ProductClient


class OLXService(ProductService):
    def __init__(
        self,
        olx_client: ProductClient
        ):
        super().__init__(
            client=olx_client
        )
