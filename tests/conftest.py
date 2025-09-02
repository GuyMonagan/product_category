import sys
import os
import pytest

# Добавляем src в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Импорт после того, как путь уже добавлен
from category import Category


@pytest.fixture(autouse=True)
def reset_class_counters():
    Category.product_count = 0
    yield
    Category.product_count = 0
