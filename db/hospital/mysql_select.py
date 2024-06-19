# внешние пакеты
from mysql.connector import connect
# стандартная библиотека
from json import loads as json_loads
from pprint import pprint
from pathlib import Path
from sys import path
# текущий проект
import queries


config_path = Path(path[0]) / 'config.json'
config = json_loads(config_path.read_text())

connection = connect(**config)

with connection.cursor() as cursor:
    cursor.execute(queries.sel_deps_wards)
    wards = cursor.fetchall()
    
    cursor.execute(queries.sel_doctors_specs)
    doctors = cursor.fetchall()

