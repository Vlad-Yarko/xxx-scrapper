from abc import abstractmethod


class ProductClient:
    @abstractmethod
    async def get_products(*args, **kwargs) -> None:
        raise NotImplementedError()

    async def get_products_all(*args, **kwargs) -> None:
        raise NotImplementedError()

    async def get_products_top(*args, **kwargs) -> None:
        raise NotImplementedError()
