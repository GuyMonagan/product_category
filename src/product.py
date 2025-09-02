from typing import Optional

class Product:
    """Класс, представляющий товар в интернет-магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация товара.

        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество в наличии
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Возвращает текущую цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Устанавливает новую цену товара.

        Если цена ≤ 0 — выводит предупреждение.
        Если цена снижается — запрашивает подтверждение.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirm = input(
                f"Вы уверены, что хотите понизить цену с {self.__price} до {new_price}? (y/n): "
            )
            if confirm.lower() != "y":
                print("Изменение отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, existing_products: Optional[list] = None):
        """
        Создаёт новый товар. Если есть товар с таким же именем — объединяет.
        """
        if existing_products is None:
            existing_products = []

        # Поиск по имени
        for prod in existing_products:
            if prod.name == product_data["name"]:
                # объединение количества
                prod.quantity += product_data["quantity"]
                # установка самой высокой цены
                if product_data["price"] > prod.price:
                    prod.price = product_data["price"]
                return prod

        # если не нашли дубликат
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )
