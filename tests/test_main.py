import os

import pytest

from src.product import Product
from src.category import Category
from src.json_loader import load_categories_from_json


@pytest.fixture
def sample_products():
    return [
        Product("Смартфон", "Мощный смартфон", 499.99, 10),
        Product("Чехол", "Силиконовый чехол", 9.99, 50)
    ]


@pytest.fixture
def sample_category(sample_products):
    # Сбросим счётчики перед созданием, чтобы избежать конфликтов между тестами
    Category.category_count = 0
    Category.product_count = 0

    return Category("Гаджеты", "Электроника и аксессуары", sample_products)


def test_product_init(sample_products):
    product = sample_products[0]
    assert product.name == "Смартфон"
    assert product.description == "Мощный смартфон"
    assert product.price == 499.99
    assert product.quantity == 10


def test_category_init(sample_category):
    assert sample_category.name == "Гаджеты"
    assert sample_category.description == "Электроника и аксессуары"
    assert len(sample_category.products) == 2


def test_category_counts(sample_category):
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_load_categories_from_json():
    filepath = os.path.join("data", "products.json")
    categories = load_categories_from_json(filepath)

    assert isinstance(categories, list)
    assert len(categories) == 2

    for category in categories:
        assert isinstance(category, Category)
        for product in category.products:
            assert isinstance(product, Product)
