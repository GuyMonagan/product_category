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

    def add_product(self, product: Product):
        """Добавляет товар в категорию и увеличивает счётчик товаров."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает строку со всеми продуктами в нужном формате."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result.strip()
