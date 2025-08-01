from src.product import Product


class Category:
    """Класс, представляющий категорию товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Инициализация категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список товаров (объекты класса Product)
        """
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
