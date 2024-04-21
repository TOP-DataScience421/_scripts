def divider(num1: float, num2: float) -> float:
    """Выполняет деление чисел используя в т. ч. специальные объекты для обозначения бесконечности."""
    try:
        return num1 / num2
    except ZeroDivisionError:
        return float(f'{"+-"[num1<0]}inf')


# >>> divider()
# TypeError: divider() missing 2 required positional arguments: 'num1' and 'num2'
# >>>
# >>> divider(10)
# TypeError: divider() missing 1 required positional argument: 'num2'
# >>>
# >>> divider(10, 5)
# 2.0
# >>>
# >>> divider(10, 5, 4)
# TypeError: divider() takes 2 positional arguments but 3 were given


def example(pos_key1, pos_key2):
    print(f'{pos_key1 = }')
    print(f'{pos_key2 = }')


# >>> example('первый аргумент', 'второй аргумент')
# pos_key1 = 'первый аргумент'
# pos_key2 = 'второй аргумент'
# >>>
# >>> example(pos_key1='первый аргумент', pos_key2='второй аргумент')
# pos_key1 = 'первый аргумент'
# pos_key2 = 'второй аргумент'
# >>>
# >>> example(pos_key2='второй аргумент', pos_key1='первый аргумент')
# pos_key1 = 'первый аргумент'
# pos_key2 = 'второй аргумент'

