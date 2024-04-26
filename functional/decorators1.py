def decorator(func_obj: 'function') -> 'function':
    """Декоратор."""
    print('начало вызова функции-декоратора')
    def wrapper(*args, **kwargs) -> 'any':
        """Обёртка."""
        print('начало вызова функции-обёртки')
        result = func_obj(*args, **kwargs)
        print('конец вызова функции-обёртки')
        return result
    print('конец вызова функции-декоратора')
    return wrapper


def test_func() -> None:
    """Тестовая функция."""
    print('вызов тестовой функции')


# >>> test_func
# <function test_func at 0x000001F707DEEFC0>
# >>>
# >>> test_func.__name__
# 'test_func'
# >>>
# >>> test_func.__doc__
# 'Тестовая функция.'
# >>>
# >>> test_func()
# вызов тестовой функции
# >>>
# >>>
# >>> test_func = decorator(test_func)
# начало вызова функции-декоратора
# конец вызова функции-декоратора
# >>>
# >>> test_func
# <function decorator.<locals>.wrapper at 0x000001F707DEF100>
# >>>
# >>> test_func.__name__
# 'wrapper'
# >>>
# >>> test_func.__doc__
# 'Обёртка.'
# >>>
# >>> test_func()
# начало вызова функции-обёртки
# вызов тестовой функции
# конец вызова функции-обёртки


# >>> len = decorator(len)
# начало вызова функции-декоратора
# конец вызова функции-декоратора
# >>>
# >>> len
# <function decorator.<locals>.wrapper at 0x000001F707DEF1A0>
# >>>
# >>> len([1, 2, 5, 7])
# начало вызова функции-обёртки
# конец вызова функции-обёртки
# 4


@decorator
def polynom(x: float, /, *, a: float, b: float, c: float) -> float:
    """Вычисляет квадратичный многочлен."""
    return a*x**2 + b*x + c


# >>> polynom
# <function decorator.<locals>.wrapper at 0x00000243C409F100>
# >>>
# >>> polynom(2, a=1, b=-3, c=5)
# начало вызова функции-обёртки
# конец вызова функции-обёртки
# 3

