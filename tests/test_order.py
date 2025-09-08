from src.order import Order
from src.product import Product


def test_order_total_price():
    p = Product("Книга", "Учебник", 500, 2)
    o = Order(product=p, quantity=3)
    assert o.total_price == 1500
    assert o.get_info() == "Книга x 3 = 1500 руб."
