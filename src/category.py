from typing import Any
from src.product import Product


class Category:
    name: str
    description: str
    __products: list[Product]

    categories_quantity = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.categories_quantity += 1
        Category.product_count += sum(product.quantity for product in products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."

    def add_product(self, new_product: Any):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            self.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        result = ''
        for i in self.__products:
            result += f'{i.name}, {i.price} руб. Остаток: {i.quantity} шт.\n'
        return result

    @property
    def get_products(self):
        return self.__products
