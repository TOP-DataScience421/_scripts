# приведёт к ModuleNotFoundError
# import _poker

import sys

print(type(sys.path), *sys.path, sep='\n', end='\n\n')

dir_path = r'D:\G-Doc\TOP Academy\Data Science\421\scripts\functional'

sys.path.insert(1, dir_path)

import _poker as p

# <class 'list'>
# D:\G-Doc\TOP Academy\Data Science\421\scripts\namespaces
# C:\Python312\python312.zip
# C:\Python312\DLLs
# C:\Python312\Lib
# C:\Python312
# C:\Python312\Lib\site-packages

# >>> p
# <module '_poker' from '...\\functional\\_poker.py'>
# >>>
# >>> p.__name__
# '_poker'

# >>> p.poker_comb((3, 4, 5, 6, 7))
# 'стрит'

