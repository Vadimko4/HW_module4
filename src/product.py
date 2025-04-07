from src.baseproduct import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    __price: float
    quantity: int

    products_list: list = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)
        Product.products_list.append(self)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, product_property: dict):
        for product in cls.products_list:
            if product.name == product_property['name']:
                product.__price = max(product.__price, product_property['price'])
                product.quantity += product_property['quantity']
                print('Такой продукт уже есть')
                return product

        new_prod = Product(product_property['name'],
                           product_property['description'],
                           product_property['price'],
                           product_property['quantity'])

        cls.products_list.append(new_prod)
        return new_prod

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price < self.__price:
                answ = input('Новая цена ниже предыдущей. Вы уверены? (y - да, любой другой ответ - нет): ')
                if answ == 'y':
                    self.__price = new_price
                else:
                    print('Цена не поменялась')
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is type(self):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is type(self):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError
