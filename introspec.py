import sys
import inspect


class introspection_info:

    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        d = {}
        d["type"] = type(self.obj).__name__  # тип ообъекта
        attributes = [attr for attr in dir(self.obj) if not attr.startswith('__')]  # исключаем системные атрибуты
        d["attributes"] = attributes  # аттрибуты
        d["methods"] = dir(self.obj)  # методы
        d["module"] = inspect.getmodule(introspection_info).__name__  # Модуль, к которому объект принадлежит
        d["size"] = f"{sys.getsizeof(self.obj)} bytes"  # размер объекта в байтах
        return f"{d}"


def x(x=1):
    pass


class intro_class:
    def __init__(self, a):
        self.a = a


intro = intro_class(1)

number_info = introspection_info(42)
print(number_info)

number_info = introspection_info("42")
print(number_info)

number_info = introspection_info(4.2)
print(number_info)

number_info = introspection_info([4, 2])
print(number_info)

number_info = introspection_info({4: 2})
print(number_info)

number_info = introspection_info(x)
print(number_info)

number_info = introspection_info(intro)
print(number_info)

number_info = introspection_info(sys)
print(number_info)

number_info = introspection_info(number_info)
print(number_info)

# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
