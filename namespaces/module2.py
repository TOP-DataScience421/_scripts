"""
Вспомогательный модуль 1.
"""

print('начало выполнения вспомогательного модуля 1')

var = 570

from module3 import func

print({
    identificator: obj
    for identificator, obj in globals().items()
    if not identificator.startswith('_')
})

print('конец выполнения вспомогательного модуля 1')
