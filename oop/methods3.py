from pathlib import Path
from pprint import pprint
from sys import path


class FileSystemIO:
    default_path = Path(path[0])
    
    @classmethod
    def read_text(cls, path: str | Path) -> str:
        if not Path(path).anchor:
            path = cls.default_path / path
        with open(path, encoding='utf-8') as filein:
            return filein.read()
    
    @classmethod
    def read_binary(cls, path: str | Path) -> bytes:
        if not Path(path).anchor:
            path = cls.default_path / path
        with open(path, 'rb') as filein:
            return filein.read()


# >>> FileSystemIO.read_text
# <bound method FileSystemIO.read_text of <class '__main__.FileSystemIO'>>

f1 = FileSystemIO()

# >>> f1.read_text
# <bound method FileSystemIO.read_text of <class '__main__.FileSystemIO'>>

# при обращении к декорированной как классовый метод функции во внутреннем пространстве имён класса от объекта и от экземпляра этого класса происходит подмена объекта функции объектом метода

FileSystemIO.read_text(r'..\git1.txt')
f1.read_text(r'..\git1.txt')

# общий вид работы связанного метода:
# class.method(*args, **kwargs) --> class.method(class, *args, **kwargs)
# instance.method(*args, **kwargs) --> instance.__class__.method(instance.__class__, *args, **kwargs)

