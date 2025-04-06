import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


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


@pytest.fixture()
def third_test_product():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14
    )


@pytest.fixture()
def test_first_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                      180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")


@pytest.fixture()
def test_second_smartphone():
    return Smartphone("Iphone 15", "512GB, Gray space",
                      210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture()
def test_first_lawngrass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0,
                     20, "Россия", "7 дней", "Зеленый")


@pytest.fixture()
def test_second_lawngrass():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15,
                     "США", "5 дней", "Темно-зеленый")
