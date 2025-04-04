
def test_product_init(first_test_product, second_test_product):
    assert first_test_product.name == "Samsung Galaxy C23 Ultra"
    assert first_test_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_test_product.price == 180000.0
    assert first_test_product.quantity == 5

    assert second_test_product.name == "Iphone 15"
    assert second_test_product.description == "512GB, Gray space"
    assert second_test_product.price == 210000.0
    assert second_test_product.quantity == 8


def test_product_str(first_test_product, second_test_product):
    assert str(first_test_product) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(second_test_product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_price_property(first_test_product, second_test_product):
    assert first_test_product.price == 180000.0
    assert second_test_product.price == 210000.0


def test_product_price_setter(first_test_product):
    assert first_test_product.price == 180000.0
    first_test_product.price = 185000.0
    assert first_test_product.price == 185000.0
