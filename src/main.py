import json

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)


def load_categories_from_json(filepath: str) -> list[Category]:
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


if __name__ == "__main__":
    categories = load_categories_from_json("data/products.json")
    for category in categories:
        print(f"{category.name} ({len(category.products)} товаров)")
