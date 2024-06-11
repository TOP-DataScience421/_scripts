# >>> dict_of_ranges = {
# ...     (1, 10): 'первый диапазон',
# ...     (11, 20): 'второй диапазон',
# ...     (21, 30): 'третий диапазон',
# ... }
# >>> dict_of_ranges[5] 
# 'первый диапазон'
# >>> dict_of_ranges[(1, 10)]
# 'первый диапазон'

from collections.abc import Iterable
from numbers import Real


class DictOfRanges(dict):
    @staticmethod
    def __check_key(key) -> bool:
        if isinstance(key, tuple):
            if len(key) == 2:
                n1, n2 = key
                if isinstance(n1, Real) and isinstance(n2, Real):
                    if n1 < n2:
                        return True
        return False
    
    # d = {'a': 1, 'b': 2}
    # d = dict(a=1, b=2)
    # d = dict([('a', 1), ('b', 2)])
    def __new__(cls, *args, **kwargs):
        if kwargs:
            raise ValueError
        if isinstance(args[0], dict):
            items = args[0].items()
        elif isinstance(args[0], Iterable):
            items = args[0]
        else:
            raise ValueError
        for key, val in items:
            if not cls.__check_key(key):
                raise ValueError
        return super().__new__(cls, *args, **kwargs)
    
    # dict.fromkeys(['a', 'b'])
    ...
    
    # d.update({'c': 3})
    ...
    
    # d |= {'c': 3}
    ...
    
    # d['c'] = 3
    def __setitem__(self, key, value):
        if self.__check_key(key):
            return super().__setitem__(key, value)
        else:
            raise ValueError
    
    # d.setdefault('c')
    ...
    
    def __getitem__(self, user_key: Real | tuple[Real, Real]):
        if isinstance(user_key, Real):
            for true_key, value in self.items():
                n1, n2 = true_key
                if n1 <= user_key <= n2:
                    return value
            else:
                raise KeyError
        else:
            return super().__getitem__(user_key)


# >>> DictOfRanges({'a': 1, 'b': 2})
# ...
# ValueError

# >>> DictOfRanges(a=1, b=2)
# ...
# ValueError

# >>> DictOfRanges([('a', 1), ('b', 2)])
# ...
# ValueError

# >>> DictOfRanges([((2, 4), 1), ((3, 5), 2)])
# {(2, 4): 1, (3, 5): 2}


dict_of_ranges = DictOfRanges({
    (1, 10): 'первый диапазон',
    (11, 20): 'второй диапазон',
    (21, 30): 'третий диапазон',
})

# >>> dict_of_ranges['c'] = 3
# ...
# ValueError
# >>>
# >>> dict_of_ranges
# {(1, 10): 'первый диапазон', (11, 20): 'второй диапазон', (21, 30): 'третий диапазон'}

# >>> dict_of_ranges[(31, 40)] = 'четвёртый диапазон'
# >>> dict_of_ranges
# {(1, 10): 'первый диапазон', (11, 20): 'второй диапазон', (21, 30): 'третий диапазон', (31, 40): 'четвёртый диапазон'}

# >>> dict_of_ranges[5]
# 'первый диапазон'
# >>>
# >>> dict_of_ranges[12]
# 'второй диапазон'
# >>>
# >>> dict_of_ranges[25]
# 'третий диапазон'
# >>>
# >>> dict_of_ranges[(31, 40)]
# 'четвёртый диапазон'
# >>>
# >>> dict_of_ranges[60]
# ...
# KeyError
# >>>
# >>> dict_of_ranges['as']
# ...
# KeyError: 'as'
