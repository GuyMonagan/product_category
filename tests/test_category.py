from src.category import Category
from src.product import Product


def test_products_getter_format_and_order():
    p1 = Product("Йогурт", "Клубничный", 80, 10)
    p2 = Product("Молоко", "1 л", 60, 5)
    cat = Category("Молочка", "Молочные продукты", [p1, p2])

    expected = "Йогурт, 80 руб. Остаток: 10 шт.\nМолоко, 60 руб. Остаток: 5 шт."
    assert cat.formatted_products() == expected


def test_add_product_appends_and_increments_counter():
    p1 = Product("Телефон", "Смарт", 1000, 1)
    p2 = Product("Ноутбук", "Игровой", 5000, 2)
    cat = Category("Электроника", "Гаджеты", [p1, p2])
    assert Category.product_count == 2

    p3 = Product("Планшет", "10 дюймов", 2000, 2)
    cat.add_product(p3)
    assert Category.product_count == 3

    # Проверяем по содержимому, что товар действительно добавился
    product_names = [product.name for product in cat.products]
    assert "Планшет" in product_names

    # Можно ещё и строковое представление проверить
    assert "Планшет, 2000 руб. Остаток: 2 шт." in cat.formatted_products()


def test_category_str_variants():
    c1 = Category(
        "Периферия",
        "desc",
        [
            Product("Мышка", "desc", 100, 4),
            Product("Клава", "desc", 200, 6),
        ],
    )
    c2 = Category(
        "Электроника",
        "desc",
        [
            Product("Товар 1", "desc", 100, 3),
            Product("Товар 2", "desc", 50, 2),
        ],
    )

    assert str(c1) == "Периферия, количество продуктов: 10 шт."
    assert str(c2) == "Электроника, количество продуктов: 5 шт."


def test_category_iterator_protocol():
    p1 = Product("Товар A", "desc", 10, 1)
    p2 = Product("Товар B", "desc", 20, 2)
    cat = Category("Категория", "desc", [p1, p2])

    # Используем итерацию напрямую
    names = [p.name for p in cat]
    assert names == ["Товар A", "Товар B"]


def test_get_average_price():
    p1 = Product("Мышка", "Обычная", 1000, 10)
    p2 = Product("Клавиатура", "Механическая", 2000, 5)
    category = Category("Периферия", "Комплектующие", [p1, p2])

    expected = (1000 + 2000) / 2
    assert category.get_average_price() == expected


def test_get_average_price_empty_category():
    category = Category("Пустая", "Нет товаров", [])
    assert category.get_average_price() == 0.0
