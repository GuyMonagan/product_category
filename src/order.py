from abc import ABC, abstractmethod

from src.product import Product


class BaseEntity(ABC):
    @abstractmethod
    def get_info(self):
        pass


class Order(BaseEntity):
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def get_info(self):
        return f"{self.product.name} x {self.quantity} = {self.total_price} руб."
