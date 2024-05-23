class Square:
    def __init__(self, side: float):
        # взаимозависимые атрибуты
        self.__side = side
        self.__area = side**2
    
    @property
    def side(self) -> float:
        return float(self.__side)
    
    @side.setter
    def side(self, new_side: float):
        self.__side = new_side
        self.__area = new_side**2
    
    @property
    def area(self) -> float:
        return float(self.__area)
    
    @area.setter
    def area(self, new_area: float):
        self.__side = new_area**0.5
        self.__area = new_area


s1 = Square(5)

# до добавления свойств:
# >>> s1.side
# 5
# >>> s1.area
# 25
# >>>
# >>> s1.side = 7
# >>> s1.side
# 7
# >>> s1.area
# 25

# после добавления свойств:
# >>> s1.side
# 5.0
# >>> s1.area
# 25.0
# >>>
# >>> s1.side = 7
# >>> s1.side
# 7.0
# >>> s1.area
# 49.0
# >>>
# >>> s1.area = 100
# >>> s1.area
# 100.0
# >>> s1.side
# 10.0

