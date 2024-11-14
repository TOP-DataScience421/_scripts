class Neuron:
    """
    Модель искусственного нейрона с двумя входами.
    """
    def __init__(self, weight1=0, weight2=0):
        self.w1 = weight1
        self.w2 = weight2
    
    def _linear(self, x1, x2):
        """Линейное преобразование входных данных. Сумматор."""
        return x1 * self.w1 + x2 * self.w2
    
    def _non_linear(self, x, cutoff=0):
        """Нелинейное преобразование. Функция Хэвисайда (ступенька)."""
        if x <= cutoff:
            return 0
        else:
            return 1
    
    def out(self, x1, x2):
        return self._non_linear(self._linear(x1, x2))



temperatures_day1 = (6, 7)
temperatures_day2 = (7, 9)
temperatures_day3 = (9, 8)

# выходы:
# 0 - похолодание
# 1 - потепление

# подбор весов — обучение
weather = Neuron(-1, 1)

# >>> weather.out(*temperatures_day1)
# 1
# >>> weather.out(*temperatures_day2)
# 1
# >>> weather.out(*temperatures_day3)
# 0

