from pprint import pprint


class Fruit:
    name: str = 'фрукт'
    color: str
    weight: float


# >>> Fruit
# <class '__main__.Fruit'>
# >>>
# >>> Fruit.__name__
# 'Fruit'

# >>> pprint(Fruit.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               '__annotations__': {'name': <class 'str'>,
#                                   'color': <class 'str'>,
#                                   'weight': <class 'float'>},
#               'name': 'фрукт',
#               '__dict__': <attribute '__dict__' of 'Fruit' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Fruit' objects>,
#               '__doc__': None})

Fruit.attr = 'атрибут класса'

# >>> pprint(Fruit.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               '__annotations__': {'name': <class 'str'>,
#                                   'color': <class 'str'>,
#                                   'weight': <class 'float'>},
#               'name': 'фрукт',
#               '__dict__': <attribute '__dict__' of 'Fruit' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Fruit' objects>,
#               '__doc__': None,
#               'attr': 'атрибут класса'})

apple = Fruit()

# >>> apple
# <__main__.Fruit object at 0x0000017E3A147440>
# >>> apple.__dict__
# {}

apple.name = 'яблоко'
apple.color = 'зелёное'
apple.weight = 0.150

# >>> apple.__dict__
# {'name': 'яблоко', 'color': 'зелёное', 'weight': 0.15}

peach = Fruit()
peach.name = 'персик'
peach.color = 'оранжевый'
peach.weight = 0.180

# >>> peach.__dict__
# {'name': 'персик', 'color': 'оранжевый', 'weight': 0.18}

# >>> apple.__class__
# <class '__main__.Fruit'>
# >>>
# >>> peach.__class__
# <class '__main__.Fruit'>
# >>>
# >>> Fruit is apple.__class__ is peach.__class__
# True

fruits = [apple, peach]
for fruit in fruits:
    print(f'{fruit.color} {fruit.name} весит {fruit.weight} кг')

# зелёное яблоко весит 0.15 кг
# оранжевый персик весит 0.18 кг

pear = Fruit()
pear.n = 'груша'
pear.colorized = 'зеленовато-жёлтая'
pear.mass = 0.12

# >>> pear.__dict__
# {'n': 'груша', 'colorized': 'зеленовато-жёлтая', 'mass': 0.12}

fruits.append(pear)
for fruit in fruits:
    print(f'{fruit.color} {fruit.name} весит {fruit.weight} кг')

# зелёное яблоко весит 0.15 кг
# оранжевый персик весит 0.18 кг
# AttributeError: 'Fruit' object has no attribute 'color'


# >>> apple.attr
# 'атрибут класса'
# >>>
# >>> apple.name
# 'яблоко'
# >>>
# >>> apple.__class__.name
# 'фрукт'
# >>>
# >>> pear.name
# 'фрукт'
# >>>
# >>> pear.__class__.name
# 'фрукт'

