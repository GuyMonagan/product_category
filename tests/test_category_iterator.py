from src.product import Product
from src.category_iterator import CategoryIterator
from src.category import Category

def test_category_iterator():
    products = [
        Product("Товар 1", "desc", 100, 3),
        Product("Товар 2", "desc", 50, 2),
    ]
    cat = Category("Категория", "desc", products)
    iterator = CategoryIterator(cat)

    iterated = [p.name for p in iterator]
    assert iterated == ["Товар 1", "Товар 2"]
