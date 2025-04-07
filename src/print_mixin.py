class PrintMixin:

    def __init__(self, *args, **kwargs):
        print(self.__repr__(self, args, kwargs))

    def __repr__(self, *args, **kwargs):
        return f"{self.__class__.__name__}, {*args, }, {*kwargs, }"
    # от какого класса и с какими параметрами был создан объект.
