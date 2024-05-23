from pathlib import Path
from pprint import pprint
from sys import path


script_dir = Path(path[0])


class FileSystemIO:
    @staticmethod
    def read_text(path: str | Path) -> str:
        if not Path(path).anchor:
            path = script_dir / path
        with open(path, encoding='utf-8') as filein:
            return filein.read()
    
    @staticmethod
    def read_binary(path: str | Path) -> bytes:
        if not Path(path).anchor:
            path = script_dir / path
        with open(path, 'rb') as filein:
            return filein.read()


# >>> pprint(FileSystemIO.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               'read_text': <staticmethod(<function FileSystemIO.read_text at 0x00000247A661EFC0>)>,
#               'read_binary': <staticmethod(<function FileSystemIO.read_binary at 0x00000247A66979C0>)>,
#               '__dict__': <attribute '__dict__' of 'FileSystemIO' objects>,
#               '__weakref__': <attribute '__weakref__' of 'FileSystemIO' objects>,
#               '__doc__': None})
# >>> 
# >>> FileSystemIO.read_text
# <function FileSystemIO.read_text at 0x00000247A661EFC0>

f1 = FileSystemIO()

# >>> f1.read_text
# <function FileSystemIO.read_text at 0x00000247A661EFC0>

# при обращении к декорированной как статический метод функции во внутреннем пространстве имён класса от экземпляра этого класса происходит обращение к самому объекту функции (без подмены)

f1.read_text('classes2.py')

