# внешние пакеты
from psycopg import connect
# стандартная библиотека
from json import loads as json_loads
from pprint import pprint
from pathlib import Path
from sys import path
# текущий проект
import queries


config_path = Path(path[0]) / 'config_psql.json'
config = json_loads(config_path.read_text())

connection = connect(**config)

with connection.cursor() as cursor:
    cursor.execute(queries.sel_deps_wards_count)
    deps_wards = cursor.fetchall()
    
    cursor.execute(queries.sel_vacation_days_by_weeks)
    vacation_days = cursor.fetchall()

# >>> pprint(deps_wards)
# [('Неврологическое отделение', 4),
#  ('Кардиологическое отделение', 4),
#  ('Физиотерапевтическое отделение', 3),
#  ('Отделение общей терапии', 3),
#  ('Отделение функциональной диагностики', 3),
#  ('Реанимация и интенсивная терапия', 3),
#  ('Токсикологическое отделение', 2)]

# >>> vacation_days
# [('больше 2 недель', 101), ('до 1 недели', 45), ('от 1 до 2 недель', 104)]

