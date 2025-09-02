from category import Category
from product import Product


def test_products_getter_format_and_order():
    p1 = Product("Йогурт", "Клубничный", 80, 10)
    p2 = Product("Молоко", "1 л", 60, 5)
    cat = Category("Молочка", "Молочные продукты", [p1, p2])

    expected = (
        "Йогурт, 80 руб. Остаток: 10 шт.\n"
        "Молоко, 60 руб. Остаток: 5 шт."
    )
    assert cat.products == expected


def test_add_product_appends_and_increments_counter():
    p1 = Product("Телефон", "Смарт", 1000, 1)
    p2 = Product("Ноутбук", "Игровой", 5000, 2)
    cat = Category("Электроника", "Гаджеты", [p1, p2])
    assert Category.product_count == 2

    p3 = Product("Планшет", "10 дюймов", 2000, 2)
    cat.add_product(p3)
    # После добавления стало на 1 больше
    assert Category.product_count == 3

    # Геттер отражает новый товар
    assert "Планшет, 2000 руб. Остаток: 2 шт." in cat.products
