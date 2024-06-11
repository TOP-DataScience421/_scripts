class Battery(int):
    def __new__(cls, capacity: int, value: int = 0):
        instance = super().__new__(cls, value)
        instance.capacity = capacity
        return instance
    
    def __repr__(self):
        return f'<{super().__repr__()}/{self.capacity}>'
    
    def __iadd__(self, other: int):
        if isinstance(other, int):
            new_value = self + other
            if new_value > self.capacity:
                new_value = self.capacity
            return self.__class__(self.capacity, new_value)
        else:
            raise TypeError
    
    # self -= other
    def __isub__(self, other: int):
        ...


b1 = Battery(10)

# >>> b1
# <0/10>
# >>> b1.__class__
# <class '__main__.Battery'>
# >>>
# >>> b1 += 5
# >>> b1
# <5/10>
# >>> b1.__class__
# <class '__main__.Battery'>
# >>>
# >>> b1 += 10
# >>> b1
# <10/10>
# >>> b1.__class__
# <class '__main__.Battery'>
