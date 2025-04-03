def test_category_init(test_category, first_test_product, second_test_product):
    assert test_category.name == "Смартфоны"
    assert test_category.description == \
           "Смартфоны, средство коммуникации и получение дополнительных функций для удобства жизни"
    assert test_category.get_products == [first_test_product, second_test_product]

    assert test_category.categories_quantity == 1
    assert test_category.product_count == 2


def test_category_products_property(test_category):
    assert test_category.products == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                      'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n')


def test_category_add_product(test_category, first_test_product, second_test_product, third_test_product):
    test_category.add_product(third_test_product)
    assert test_category.get_products == [first_test_product, second_test_product, third_test_product]
