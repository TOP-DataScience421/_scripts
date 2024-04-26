def test_generator() -> 'generator':
    print('начало выполнения тела генераторной функции')
    yield 3
    print('второй шаг выполнения тела генераторной функции')
    yield 2
    print('третий шаг выполнения тела генераторной функции')
    yield 1
    print('четвёртый шаг выполнения тела генераторной функции')
    yield 0
    print('конец выполнения тела генераторной функции')


# >>> generator_obj = test_generator()
# >>>
# >>> generator_obj
# <generator object test_generator at 0x000001DAB85456C0>
# >>>
# >>> generator_obj.__next__()
# начало выполнения тела генераторной функции
# 3
# >>> generator_obj.__next__()
# второй шаг выполнения тела генераторной функции
# 2
# >>> elem = generator_obj.__next__()
# третий шаг выполнения тела генераторной функции
# >>> elem
# 1
# >>> elem = generator_obj.__next__()
# четвёртый шаг выполнения тела генераторной функции
# >>> elem
# 0
# >>> generator_obj.__next__()
# конец выполнения тела генераторной функции
# StopIteration
# >>>
# >>> generator_obj.__next__()
# StopIteration
# >>>
# >>>
# >>> for elem in generator_obj:
# ...     print(elem)
# ...
# >>>

