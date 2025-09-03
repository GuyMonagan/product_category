import pytest

from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone


def test_smartphone_init():
    s = Smartphone("iPhone", "desc", 100_000, 3, "A16", "14 Pro", "512GB", "space gray")
    assert s.name == "iPhone"
    assert s.model == "14 Pro"
    assert s.memory == "512GB"


def test_lawn_grass_init():
    g = LawnGrass("Газон", "desc", 500, 10, "Россия", "10 дней", "зелёный")
    assert g.country == "Россия"
    assert g.germination_period == "10 дней"


def test_add_different_product_types_raises():

    p1 = Smartphone(
        "iPhone", "desc", 100_000, 3, "A16", "14 Pro", "512GB", "space gray"
    )
    p2 = LawnGrass("Газон", "desc", 500, 10, "Россия", "10 дней", "зелёный")

    with pytest.raises(TypeError):
        _ = p1 + p2


def test_add_invalid_object_to_category_raises():
    from src.category import Category

    c = Category("Test", "desc", [])
    with pytest.raises(TypeError):
        c.add_product("это не продукт")
