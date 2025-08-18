from abc import abstractmethod


class ProductClient:
    @abstractmethod
    async def get_products(*args, **kwargs) -> None:
        raise NotImplementedError()
