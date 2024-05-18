from pathlib import Path
from sys import path

script_dir = Path(path[0])
data_path = script_dir / 'data.txt'
log_path = script_dir / 'log'

filein = open(data_path)

# >>> filein
# <_io.TextIOWrapper name='...\\files\\data.txt' mode='r' encoding='cp1251'>
# >>>
# >>> type(filein)
# <class '_io.TextIOWrapper'>
# >>>
# >>> filein.read()
# 'РїРµСЂРІР°СЏ СЃС‚СЂРѕС‡РєР°\nРІС‚РѕСЂР°СЏ СЃС‚СЂРѕС‡РєР°\nС‚СЂРµС‚СЊСЏ СЃС‚СЂРѕС‡РєР°'

filein.close()

filein = open(data_path, encoding='utf-8')

# >>> filein
# <_io.TextIOWrapper name='...\\files\\data.txt' mode='r' encoding='utf-8'>
# >>>
# >>> filein.readline()
# 'первая строчка\n'
# >>>
# >>> filein.readlines()
# ['вторая строчка\n', 'третья строчка']

filein.close()

with open(log_path, encoding='utf-8') as filein:
    data = filein.readlines()

from datetime import datetime as dt

dates = [
    dt.strptime(elem.rstrip(), '%Y/%m/%d - %H:%M:%S')
    for elem in data
]
