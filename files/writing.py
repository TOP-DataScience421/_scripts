from datetime import datetime as dt

import reading as paths

lines = [
    'новая первая строчка\n',
    'новая вторая строчка',
]

with open(paths.data_path, 'w', encoding='utf-8') as fileout:
    fileout.writelines(lines)
    fileout.write('новая третья строчка\nновая четвёртая строчка\n')
    print('новая пятая строчка', file=fileout)

cur_datetime = f'{dt.now():%Y/%m/%d - %H:%M:%S}'
with open(paths.log_path, 'a', encoding='utf-8') as fileout:
    print(cur_datetime, file=fileout)

