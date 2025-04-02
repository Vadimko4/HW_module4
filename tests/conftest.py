import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def test_category(first_test_product, second_test_product):
    return Category(
        name="Смартфоны",
        description="Смартфоны, средство коммуникации и получение дополнительных функций для удобства жизни",
        products=[first_test_product, second_test_product]
    )


@pytest.fixture()
def first_test_product():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture()
def second_test_product():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )
