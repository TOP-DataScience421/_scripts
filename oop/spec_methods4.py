from numbers import Real


class Hero:
    def __init__(self, name: str):
        self.name = name
        self.health: float = 100
    
    def __repr__(self):
        return f'<{self.name}: {self.health}/100>'
    
    # self + other
    def __add__(self, other):
        return self.health + other
    
    # other + self
    def __radd__(self, other):
        return self.__add__(other)
    
    # -self
    def __neg__(self):
        return -self.health
    
    # self - other
    def __sub__(self, other):
        return self.health - other
    
    # other - self
    def __rsub__(self, other):
        return -self.health + other
    
    # self += other
    def __iadd__(self, other):
        self.health += other
        return self
    
    # self -= other
    def __isub__(self, other):
        self.health -= other
        return self


konung = Hero('Олег')

# >>> konung
# <Олег: 100/100>
# >>>
# >>> konung + 50
# 150
# >>> konung
# <Олег: 100/100>
# >>>
# >>> konung + 'abc'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>>
# >>> 40 + konung
# 140
# >>> konung
# <Олег: 100/100>
# >>>
# >>> [1, 2] + konung
# TypeError: unsupported operand type(s) for +: 'int' and 'list'
# >>>
# >>> konung -= 12
# >>> konung
# <Олег: 88/100>
# >>>
# >>> konung += 4
# >>> konung
# <Олег: 92/100>

