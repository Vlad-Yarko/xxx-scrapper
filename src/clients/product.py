from abc import abstractmethod

from src.utils.client import Client


class ProductClient(Client):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError()

    @abstractmethod
    async def open_session(*args, **kwargs) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def close_session(*args, **kwargs) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def get_products(*args, **kwargs) -> None:
        raise NotImplementedError()
