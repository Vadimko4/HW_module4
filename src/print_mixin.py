class PrintMixin:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}, {', '.join(str(i) for i in self.__dict__.values())}"
    # от какого класса и с какими параметрами был создан объект.
