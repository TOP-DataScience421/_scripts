func_object1 = lambda: print('вызов')
func_object2 = lambda n1, n2: (n1 + n2) / 2


# >>> func_object1()
# вызов
# >>> var = func_object1()
# вызов
# >>> type(var)
# <class 'NoneType'>
# >>>
# >>>
# >>> func_object2()
# TypeError: <lambda>() missing 2 required positional arguments: 'n1' and 'n2'
# >>>
# >>> func_object2(3, 5)
# 4.0
# >>> var = func_object2(3, 5)
# >>>
# >>> type(var)
# <class 'float'>


# >>> func_object1
# <function <lambda> at 0x000001E202DF8A40>
# >>>
# >>> func_object2
# <function <lambda> at 0x000001E20321EFC0>
# >>>
# >>>
# >>> type(func_object1)
# <class 'function'>
# >>>
# >>> type(func_object2)
# <class 'function'>
# >>>
# >>>
# >>> id(func_object1)
# 2070222441024
# >>>
# >>> id(func_object2)
# 2070226792384
# >>>
# >>>
# >>> func_object1.__name__
# '<lambda>'
# >>>
# >>> func_object2.__name__
# '<lambda>'

