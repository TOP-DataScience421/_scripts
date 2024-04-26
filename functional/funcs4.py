def concat(*strings: str, sep: str = ', ') -> str:
    print(type(strings), strings)
    return sep.join(strings)


# >>> concat()
# <class 'tuple'> ()
# ''
# >>>
# >>> concat('ABC')
# <class 'tuple'> ('ABC',)
# 'ABC'
# >>>
# >>> concat('abc', 'def')
# <class 'tuple'> ('abc', 'def')
# 'abc, def'
# >>>
# >>> concat('1', '2', '3', '5', sep=' ')
# <class 'tuple'> ('1', '2', '3', '5')
# '1 2 3 5'
# >>>
# >>> numbers = [str(n) for n in range(10, 100, 10)]
# >>> concat(*numbers)
# <class 'tuple'> ('10', '20', '30', '40', '50', '60', '70', '80', '90')
# '10, 20, 30, 40, 50, 60, 70, 80, 90'
# >>>
# >>> concat('5', *numbers, '100')
# <class 'tuple'> ('5', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100')
# '5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100'
# >>>
# >>> concat(*numbers, sep='—')
# <class 'tuple'> ('10', '20', '30', '40', '50', '60', '70', '80', '90')
# '10—20—30—40—50—60—70—80—90'


def mean(num1: float, num2: float, *numbers: float) -> float:
    print(f'{num1=}\t{num2=}\t{numbers=}')
    numbers = num1, num2, *numbers
    print(f'{numbers=}')
    return sum(numbers) / len(numbers)


# >>> mean()
# TypeError: mean() missing 2 required positional arguments: 'num1' and 'num2'
# >>>
# >>> mean(1, 2)
# num1=1  num2=2  numbers=()
# numbers=(1, 2)
# 1.5
# >>>
# >>> mean(1, 2, 3, 4)
# num1=1  num2=2  numbers=(3, 4)
# numbers=(1, 2, 3, 4)
# 2.5
# >>>
# >>> numbers = range(3, 30, 3)
# >>> mean(*numbers)
# num1=3  num2=6  numbers=(9, 12, 15, 18, 21, 24, 27)
# numbers=(3, 6, 9, 12, 15, 18, 21, 24, 27)
# 15.0

