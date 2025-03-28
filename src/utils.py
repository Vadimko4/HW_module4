import json
import os

from src.category import Category
from src.product import Product


def read_categories_dict_from_json(path: str) -> list[dict]:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        dicts_list = json.load(file)
    return dicts_list


def create_objects_from_dicts_list(data_list) -> list[Category]:
    categories_list = []
    for item in data_list:
        products_list = []
        for i in item.get('products'):
            product = Product(**i)
            # Product(i.get('name'), i.get('description'), i.get('price'), i.get('quantity'))
            products_list.append(product)
        item['products'] = products_list
        # category = Category(item.get('name'), item.get('descriptiondescription'), products_list)
        categories_list.append(Category(**item))

    return categories_list


# if __name__ == "__main__":
#     dicts = read_categories_dict_from_json('../data/products.json')
#     categories = create_objects_from_dicts_list(dicts)
#     print(categories)
#     print(categories[0].name)
#     print(categories[0].products)
#     print(categories[0].categories_quantity)
#     print(categories[0].products_quantity)
