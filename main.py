from src.json_loader import load_categories_from_json
from src.category_iterator import CategoryIterator


def main():
    """
    Точка входа в программу.

    Загружает категории из JSON-файла и выводит количество товаров в каждой из них.
    """
    categories = load_categories_from_json("data/products.json")
    for category in categories:
        print(f"{category.name} ({len(category.products)} товаров)")

        print("Список товаров:")
        print(category.formatted_products())

if __name__ == "__main__":
    main()

