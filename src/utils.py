import os

import json
from src.category import Category


def read_categories_dict_from_json(path: str) -> list[dict]:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        dicts_list = json.load(file)
    return dicts_list


