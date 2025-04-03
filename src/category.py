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
        Category.product_count += len(products)

    def add_product(self, product: Product):
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self):
        result = ''
        for i in self.__products:
            result += f'{i.name}, {i.price} руб. Остаток: {i.quantity} шт.\n'
        return result

    @property
    def get_products(self):
        return self.__products
