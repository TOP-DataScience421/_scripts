path1 = 'c:\\users\\username'
path2 = r'd:\network\project\scripts'
print(path1, path2, sep='\n', end='\n\n')

from pathlib import Path
from sys import path

# current working directory — текущий рабочий каталог
path3 = Path.cwd()
path4 = Path(r'c:\windows')
path5 = Path(path[0])
print(path3, path5, sep='\n', end='\n\n')

# конструирование путей
path6 = path5 / 'data.txt'
path7 = path5 / 'log'
path8 = path7 / 'journals.log'
print(path6, path7, sep='\n', end='\n\n')

# >>> path5.name
# 'files'
# >>> path6.name
# 'data.txt'
# >>> path7.name
# 'log'
# >>>
# >>> path5.suffix
# ''
# >>> path6.suffix
# '.txt'
# >>> path7.suffix
# ''

# обращение к файловой системе
# >>> path5.exists()
# True
# >>> path5.is_file()
# False
# >>> path5.is_dir()
# True
# >>>
# >>> path6.exists()
# True
# >>> path6.is_file()
# True
# >>> path6.is_dir()
# False
# >>>
# >>> path7.exists()
# True
# >>> path7.is_file()
# True
# >>> path7.is_dir()
# False
# >>>
# >>> path8.exists()
# False
# >>> path8.is_file()
# False
# >>> path8.is_dir()
# False

# >>> path5.iterdir()
# <generator object Path.iterdir at 0x000001DDDC8FEC20>
# >>> 
# >>> for p in path5.iterdir():
# ...     print(p)
# ...
# D:\G-Doc\TOP Academy\Data Science\421\scripts\files\data.txt
# D:\G-Doc\TOP Academy\Data Science\421\scripts\files\log
# D:\G-Doc\TOP Academy\Data Science\421\scripts\files\paths.py
