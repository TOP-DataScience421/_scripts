class Person:
    def __init__(self, last_name, first_name, patr_name):
        self.last = last_name
        self.first = first_name
        self.patr = patr_name
    
    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.first[0]}.{self.patr[0]}.{self.last}>'
    
    def __str__(self):
        return f'{self.last} {self.first} {self.patr}'


teacher = Person('Шаповаленко', 'Геннадий', 'Дмитриевич')

# >>> teacher
# <Person: Г.Д.Шаповаленко>
# >>>
# >>> print(teacher)
# Шаповаленко Геннадий Дмитриевич

# >>> repr(teacher)
# '<Person: Г.Д.Шаповаленко>'
# >>>
# >>> teacher.__repr__()
# '<Person: Г.Д.Шаповаленко>'
# >>>
# >>> str(teacher)
# 'Шаповаленко Геннадий Дмитриевич'
# >>>
# >>> teacher.__str__()
# 'Шаповаленко Геннадий Дмитриевич'

