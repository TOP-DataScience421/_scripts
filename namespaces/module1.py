"""
Точка входа.
"""

print('начало выполнения модуля точки входа')

import module2

print({
    identificator: obj
    for identificator, obj in globals().items()
    if not identificator.startswith('_')
})

print('конец выполнения модуля точки входа')


# начало выполнения модуля точки входа
# начало выполнения вспомогательного модуля 1
# начало выполнения вспомогательного модуля 2
# {'func': <function func at 0x0000020702C8F240>}
# конец выполнения вспомогательного модуля 2
# {'var': 570, 'func': <function func at 0x000001C60EC8F240>}
# конец выполнения вспомогательного модуля 1
# {'module2': <module 'module2' from '...\\namespaces\\module2.py'>}
# конец выполнения модуля точки входа


# >>> __name__
# '__main__'
# >>>
# >>> __doc__
# '\nТочка входа.\n'
# >>>
# >>> globals()
# {'__name__': '__main__', '__doc__': '\nТочка входа.\n', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000020702A1A120>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'module2': <module 'module2' from '...\\module2.py'>}


# >>> from sys import modules
# >>>
# >>> modules['module3']
# <module 'module3' from '...\\module3.py'>

