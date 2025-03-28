from src.utils import create_objects_from_dicts_list


def test_create_objects_from_dicts_list(test_category, first_test_product, second_test_product):
    test_dict_list = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, средство коммуникации и получение дополнительных функций для удобства жизни",
            "products":
                [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5
                    },
                    {
                        "name": "Iphone 15",
                        "description": "512GB, Gray space",
                        "price": 210000.0,
                        "quantity": 8}
                ]
        }
    ]
    test_objects_list = create_objects_from_dicts_list(test_dict_list)
    assert len(test_objects_list) == 1
    assert test_objects_list[0].name == test_category.name
    assert test_objects_list[0].description == test_category.description
    assert test_objects_list[0].products_quantity == test_category.products_quantity
    assert test_objects_list[0].categories_quantity == test_category.categories_quantity

