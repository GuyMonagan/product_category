from src.category_iterator import CategoryIterator
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
        self.__products = products  # приватный

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Добавляет строкое отображение для класса Category"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        return CategoryIterator(self)

    def add_product(self, product: Product):
        """Ограничение добавления продуктов в категорию"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product или его подклассов")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list[Product]:
        return self.__products

    def formatted_products(self) -> str:
        return "\n".join(str(p) for p in self.__products)
