import builtins

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
        "quantity": 2
    }

    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Test Product"
    assert product.quantity == 2
    assert product.price == 100

