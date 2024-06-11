from pprint import pprint


# родительский (parent), базовый (base), предок, надкласс (superclass)
class Parent:
    attr1 = 'атрибут базового класса'
    
    def __init__(self, val):
        self.inst_attr1 = val
    
    def super_method(self):
        print(f'вызов метода базового класса от {self}')


# дочерний (child), производный (inherent), потомок, подкласс (subclass)
class Child(Parent):
    attr2 = 'атрибут производного класса'
    
    def __init__(self, val):
        self.inst_attr2 = val
    
    def sub_method(self):
        print(f'вызов метода производного класса от {self}')


p1 = Parent(222)
# >>> p1
# <__main__.Parent object at 0x0000020DA3957170>

c1 = Child(444)
# >>> c1
# <__main__.Child object at 0x0000020DA39571A0>

# >>> p1.__dict__
# {'inst_attr1': 222}
# >>>
# >>> pprint(Parent.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               'attr1': 'атрибут базового класса',
#               '__init__': <function Parent.__init__ at 0x0000020DA395EFC0>,
#               'super_method': <function Parent.super_method at 0x0000020DA395F060>,
#               '__dict__': <attribute '__dict__' of 'Parent' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Parent' objects>,
#               '__doc__': None})
# >>>
# >>> c1.__dict__
# {'inst_attr2': 444}
# >>>
# >>> pprint(Child.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               'attr2': 'атрибут производного класса',
#               '__init__': <function Child.__init__ at 0x0000020DA395F100>,
#               'sub_method': <function Child.sub_method at 0x0000020DA395F1A0>,
#               '__doc__': None})

# >>> c1.inst_attr2
# 444
# >>> c1.attr2
# 'атрибут производного класса'
# >>>
# >>> c1.attr1
# 'атрибут базового класса'
# >>>
# >>> c1.sub_method
# <bound method Child.sub_method of <__main__.Child object at 0x0000020DA39571A0>>
# >>>
# >>> c1.sub_method()
# вызов метода производного класса от <__main__.Child object at 0x0000020DA39571A0>
# >>>
# >>> c1.super_method
# <bound method Parent.super_method of <__main__.Child object at 0x0000020DA39571A0>>
# >>>
# >>> c1.super_method()
# вызов метода базового класса от <__main__.Child object at 0x0000020DA39571A0>


class Child2(Parent):
    pass


# >>> c2 = Child2()
# TypeError: Parent.__init__() missing 1 required positional argument: 'val'
# >>>
# >>> Child2.__init__
# <function Parent.__init__ at 0x0000020DA395EFC0>
# >>>
# >>> c2 = Child2(446)
# >>>
# >>> c2.__dict__
# {'inst_attr1': 446}

