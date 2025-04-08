import pytest
from src.product import Product


def test_product_init(first_test_product, second_test_product):
    assert first_test_product.name == "Samsung Galaxy C23 Ultra"
    assert first_test_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_test_product.price == 180000.0
    assert first_test_product.quantity == 5

    assert second_test_product.name == "Iphone 15"
    assert second_test_product.description == "512GB, Gray space"
    assert second_test_product.price == 210000.0
    assert second_test_product.quantity == 8

    assert second_test_product.name == "Iphone 15"
    assert second_test_product.description == "512GB, Gray space"
    assert second_test_product.price == 210000.0
    assert second_test_product.quantity == 8


def test_product_init_zero_quantity():
    with pytest.raises(ValueError):
        Product("test_name", "test_description", 100000.0, 0)


def test_product_str(first_test_product, second_test_product):
    assert str(first_test_product) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(second_test_product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_add(first_test_product, second_test_product):
    assert first_test_product + second_test_product == 2580000.0


def test_product_price_property(first_test_product, second_test_product):
    assert first_test_product.price == 180000.0
    assert second_test_product.price == 210000.0


def test_product_price_setter(first_test_product):
    assert first_test_product.price == 180000.0
    first_test_product.price = 185000.0
    assert first_test_product.price == 185000.0


def test_first_smartphone_init(test_first_smartphone):
    assert test_first_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert test_first_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert test_first_smartphone.price == 180000.0
    assert test_first_smartphone.quantity == 5
    assert test_first_smartphone.efficiency == 95.5
    assert test_first_smartphone.model == "S23 Ultra"
    assert test_first_smartphone.memory == 256
    assert test_first_smartphone.color == "Серый"


def test_first_lawngrass_init(test_first_lawngrass):
    assert test_first_lawngrass.name == "Газонная трава"
    assert test_first_lawngrass.description == "Элитная трава для газона"
    assert test_first_lawngrass.price == 500.0
    assert test_first_lawngrass.quantity == 20
    assert test_first_lawngrass.country == "Россия"
    assert test_first_lawngrass.germination_period == "7 дней"
    assert test_first_lawngrass.color == "Зеленый"


def test_smartphone_add(test_first_smartphone, test_second_smartphone):
    assert (test_first_smartphone + test_second_smartphone) == 2580000.0


def test_smartphone_wrong_add(test_first_smartphone, test_first_lawngrass):
    with pytest.raises(TypeError):
        print(test_first_smartphone + test_first_lawngrass)


def test_lawngrass_add(test_first_lawngrass, test_second_lawngrass):
    assert (test_first_lawngrass + test_second_lawngrass) == 16750.0


def test_lawngrass_wrong_add(test_first_lawngrass, test_first_smartphone):
    with pytest.raises(TypeError):
        print(test_first_lawngrass + test_first_smartphone)
