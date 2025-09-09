import builtins

import pytest

from src.product import Product


def test_price_getter_and_setter_increase():
    p = Product("Йогурт", "Клубничный", 80, 10)
    p.price = 120  # повышение — без вопросов
    assert p.price == 120


def test_price_setter_non_positive_does_not_change_and_prints(capsys):
    p = Product("Молоко", "1 л", 60, 5)
    p.price = -1
    captured = capsys.readouterr().out
    assert "Цена не должна быть нулевая или отрицательная" in captured
    assert p.price == 60


def test_price_lowering_confirms_yes(monkeypatch):
    p = Product("Сыр", "Мягкий", 300, 2)
    monkeypatch.setattr(builtins, "input", lambda _: "y")
    p.price = 250  # понижение с подтверждением
    assert p.price == 250


def test_price_lowering_confirms_no(monkeypatch, capsys):
    p = Product("Сыр", "Полутвердый", 300, 2)
    monkeypatch.setattr(builtins, "input", lambda _: "n")
    p.price = 250  # попытка понижения без согласия
    captured = capsys.readouterr().out
    assert "Изменение отменено" in captured
    assert p.price == 300  # не изменилось


def test_new_product_creates_when_not_exists():
    data = {"name": "Кефир", "description": "2.5%", "price": 90, "quantity": 3}
    p = Product.new_product(data, existing_products=[])
    assert isinstance(p, Product)
    assert p.name == "Кефир"
    assert p.price == 90
    assert p.quantity == 3


def test_new_product_merges_by_name_and_picks_higher_price():
    existing = [Product("Хлеб", "Бородинский", 40, 5)]
    # Приходит товар с таким же именем, большей ценой и количеством
    data = {"name": "Хлеб", "description": "Бородинский", "price": 45, "quantity": 2}
    merged = Product.new_product(data, existing_products=existing)
    # Возвращается существующий объект
    assert merged is existing[0]
    # Кол-во сложилось
    assert merged.quantity == 7
    # Цена — более высокая
    assert merged.price == 45


def test_new_product_without_existing():
    # когда аргумент existing_products не был передан в метод
    data = {
        "name": "Test Product",
        "description": "Тестовое описание",
        "price": 100,
        "quantity": 2,
    }

    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Test Product"
    assert product.quantity == 2
    assert product.price == 100


def test_product_str_and_add():
    p1 = Product("Товар A", "Описание", 100.0, 3)
    p2 = Product("Товар B", "Описание", 200.0, 2)

    assert str(p1) == "Товар A, 100.0 руб. Остаток: 3 шт."
    assert str(p2) == "Товар B, 200.0 руб. Остаток: 2 шт."
    assert p1 + p2 == 100.0 * 3 + 200.0 * 2  # 300 + 400 = 700


def test_product_add_invalid_type():
    p = Product("X", "desc", 10, 1)
    with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
        p + "not a product"


def test_product_creation_with_zero_quantity_raises():
    with pytest.raises(ValueError) as excinfo:
        Product("Сыр", "Голландский", 250.0, 0)

    assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен"


def test_product_creation_with_valid_quantity():
    p = Product("Молоко", "1л", 90.0, 3)
    assert p.name == "Молоко"
    assert p.quantity == 3
    assert p.price == 90.0
