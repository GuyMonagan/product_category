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
        self.price = price
        self.quantity = quantity
