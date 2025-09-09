from typing import Optional

from src.base_product import BaseProduct
from src.mixins import CreationLoggerMixin


class Product(CreationLoggerMixin, BaseProduct):
    """Класс, представляющий товар в интернет-магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self._price:
            confirm = input(
                f"Вы уверены, что хотите понизить цену с {self._price} до {new_price}? (y/n): "
            )
            if confirm.lower() != "y":
                print("Изменение отменено")
                return

        self._price = new_price

    @classmethod
    def new_product(cls, product_data: dict, existing_products: Optional[list] = None):
        if existing_products is None:
            existing_products = []

        for prod in existing_products:
            if prod.name == product_data["name"]:
                prod.quantity += product_data["quantity"]
                if product_data["price"] > prod.price:
                    prod.price = product_data["price"]
                return prod

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )
