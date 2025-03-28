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
