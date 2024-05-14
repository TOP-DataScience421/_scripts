"""
Вспомогательный модуль 2.
"""

print('начало выполнения вспомогательного модуля 2')

def func() -> int:
    return -1

print({
    identificator: obj
    for identificator, obj in globals().items()
    if not identificator.startswith('_')
})

print('конец выполнения вспомогательного модуля 2')
