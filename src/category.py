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
        self.__products = products  # приватный список продуктов

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        """Позволяет итерировать по товарам в категории."""
        return CategoryIterator(self)

    def add_product(self, product: Product):
        """
        Добавляет продукт в категорию, если он является
        экземпляром Product или его наследником.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product или его подклассов")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list[Product]:
        """Возвращает список продуктов в категории."""
        return self.__products

    def formatted_products(self) -> str:
        """Возвращает строку с форматированным списком продуктов."""
        return "\n".join(str(p) for p in self.__products)

    def get_average_price(self) -> float:
        """
        Вычисляет среднюю цену всех товаров в категории.
        :return: Средняя цена, либо 0.0, если товаров нет.
        """
        if not self.__products:
            return 0.0
        total_price = sum(product.price for product in self.__products)
        return total_price / len(self.__products)
