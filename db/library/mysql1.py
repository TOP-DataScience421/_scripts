# внешние пакеты
from mysql.connector import connect
# стандартная библиотека
from json import loads as json_loads
from pathlib import Path
from pprint import pprint
from sys import path
# текущий проект
import queries


config_path = Path(path[0]) / 'config.json'
config = json_loads(config_path.read_text())


connection = connect(**config)

with connection.cursor() as cursor:
    cursor.execute(queries.select_all_authors)
    rows = cursor.fetchall()

# >>> pprint(rows)
# [(1, 'Толстой', 'Лев'),
#  (2, 'Достоевский', 'Фёдор'),
#  (3, 'Булгаков', 'Михаил'),
#  (4, 'Лукьяненко', 'Сергей'),
#  (5, 'Буджолд', 'Лоис'),
#  (6, 'Вебер', 'Дэвид')]

with connection.cursor() as cursor:
    cursor.execute(queries.select_authors_fullname)
    rows = cursor.fetchall()

# >>> pprint(rows)
# [('Лев Толстой',),
#  ('Фёдор Достоевский',),
#  ('Михаил Булгаков',),
#  ('Сергей Лукьяненко',),
#  ('Лоис Буджолд',),
#  ('Дэвид Вебер',)]

connection.close()

