import json
from src.product import Product
from src.category import Category


def load_categories_from_json(filepath: str) -> list[Category]:
    """
    Загружает список категорий и товаров из JSON-файла.

    :param filepath: Путь к JSON-файлу
    :return: Список объектов Category
    """
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []

    for cat in data:
        products = [
            Product(
                name=p["name"],
                description=p["description"],
                price=p["price"],
                quantity=p["quantity"]
            )
            for p in cat["products"]
        ]
        category = Category(
            name=cat["name"],
            description=cat["description"],
            products=products
        )
        categories.append(category)

    return categories
