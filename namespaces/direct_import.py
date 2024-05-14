# приведёт к SyntaxError
# import 1

from importlib.util import spec_from_file_location, module_from_spec
from sys import modules

file_path = r'd:\G-Doc\TOP Academy\Data Science\421\scripts\namespaces\1.py'
module_name = 'my_module'

# создание вспомогательного объекта спецификации
spec_obj = spec_from_file_location(module_name, file_path)
# создание объекта модуля и идентификатора
my_module = module_from_spec(spec_obj)

# кэширование объекта модуля
modules[module_name] = my_module

# выполнение кода модуля
spec_obj.loader.exec_module(my_module)


print(f'{my_module = }')
print(f'{my_module.var = }')

# my_module = <module 'my_module' from '...\\1.py'>
# my_module.var = 3407

