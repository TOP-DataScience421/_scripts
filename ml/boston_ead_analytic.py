from pandas import read_csv

from pathlib import Path
from sys import path


data_path = Path(path[0]) / 'boston.csv'
boston = read_csv(data_path, comment='#')

# технический обзор набора данных
boston.info()
print()

# численные характеристики переменных
print(boston.describe().round(3), end='\n\n')

# взаимосвязи между переменными
print(boston.corr().round(2), end='\n\n')

