from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех товаров."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict, existing_products: list = None):
        pass
