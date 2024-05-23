from pprint import pprint


class Liquid:
    def __init__(self, name: str, density: float):
        self.name = name
        self.density = density


# >>> pprint(Liquid.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               '__init__': <function Liquid.__init__ at 0x000001CD0232EFC0>,
#               '__dict__': <attribute '__dict__' of 'Liquid' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Liquid' objects>,
#               '__doc__': None})
# >>>
# >>> Liquid.__init__
# <function Liquid.__init__ at 0x000001CD0232EFC0>
# >>>
# >>> type(Liquid.__init__)
# <class 'function'>


# при вызове объекта класса сначала создаётся объект экземпляра, после чего он конфигурируется с помощью метода __init__()
# def metaclass.__new__(cls, *args, **kwargs):
#     instance = __new__(cls)
#     cls.__init__(instance, *args, **kwargs)
#     return instance

water = Liquid('вода', 1.0)
green_oil = Liquid('растительное масло', 0.94)

# >>> water.__dict__
# {'name': 'вода', 'density': 1.0}
# >>>
# >>> green_oil.__dict__
# {'name': 'растительное масло', 'density': 0.94}

