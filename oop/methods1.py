from pprint import pprint


class Printer:
    def __init__(self, text: str = ''):
        self.text = text
    
    def print_line(self) -> None:
        line = self.text.split('\n', 1)[0]
        print(line)
    
    def print_page(self) -> None:
        page = self.text.split('\f', 1)[0]
        print(page)


p1 = Printer('''Написать функцию высшего порядка с именем math_function_resolver, которая вычисляет округлённые значения для различных математических функций.
Функция принимает обязательным аргументом математическую функцию, произвольное количество значений x для математической функции и необязательным аргументом переключатель: тип вычисляемых значений float или str.
Математическая функция должна быть строго позиционным аргументом, передаётся в виде вызываемого объекта.
Данная функция должна принимать один обязательный позиционно-ключевой аргумент — число x, для которого необходимо вычислить значение математической функции. Это должно быть описано в документации к функции высшего порядка.
''')

# >>> Printer.print_line
# <function Printer.print_line at 0x000002039B5D76A0>
# >>>
# >>> type(Printer.print_line)
# <class 'function'>
# >>>
# >>> p1.print_line
# <bound method Printer.print_line of <__main__.Printer object at 0x000002039B587110>>
# >>>
# >>> type(p1.print_line)
# <class 'method'>

# при обращении к функции во внутреннем пространстве имён класса от экземпляра этого класса происходит подмена объекта функции объектом метода

# p1.print_line() --> Printer.print_line(p1)

# >>> p1.print_line()
# Написать функцию высшего порядка с именем math_function_resolver, которая вычисляет округлённые значения для различных математических функций.
# >>>
# >>> Printer.print_line(p1)
# Написать функцию высшего порядка с именем math_function_resolver, которая вычисляет округлённые значения для различных математических функций.

# общий вид работы связанного метода:
# instance.method(*args, **kwargs) --> instance.__class__.method(instance, *args, **kwargs)

