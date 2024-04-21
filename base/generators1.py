# <объект_генератор> = (
#     <выражение> 
#     for <переменная_цикла> in <выражение_возвращающее_итератор> 
#     if <проверочное_выражение>
# )

numbers = (int(d) for d in '0123456789')

# >>> numbers
# <generator object <genexpr> at 0x000001A73B9DC520>

for n in numbers:
    print(n, type(n))

# 0 <class 'int'>
# 1 <class 'int'>
# 2 <class 'int'>
# 3 <class 'int'>
# 4 <class 'int'>
# 5 <class 'int'>
# 6 <class 'int'>
# 7 <class 'int'>
# 8 <class 'int'>
# 9 <class 'int'>
# 
# >>> for n in numbers:
# ...     print(n)
# ...
# >>>


