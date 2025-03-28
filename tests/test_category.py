from src.category import Category


def test_category_init(test_category, first_test_product, second_test_product):
    assert test_category.name == "Смартфоны"
    assert test_category.description == \
           "Смартфоны, средство коммуникации и получение дополнительных функций для удобства жизни"
    assert test_category.products == [first_test_product, second_test_product]

    assert test_category.categories_quantity == 1
    assert test_category.products_quantity == 2
