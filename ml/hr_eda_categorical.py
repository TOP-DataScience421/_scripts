from pandas import (
    read_csv,
    Categorical,
    crosstab,
)

from itertools import count
from pathlib import Path
from sys import path


datafile_path = Path(path[0]) / 'HR.csv'
corr_table_path = Path(path[0]) / 'HR_corr_table.csv'


employees = read_csv(datafile_path, comment='#')

employees.columns = ('SLVL', 'LE', 'NP', 'AMH', 'TSC', 'WA', 'left', 'PROM5', 'DEP', 'SAL')

employees_vars = employees.describe().round(2)
# print(employees_vars, end='\n\n')

# employees['DEP'] = Categorical(employees['DEP'])
# employees['SAL'] = Categorical(employees['SAL'])


departments = dict(zip(employees['DEP'].unique(), count()))
employees['DEP'] = employees['DEP'].map(departments)

salaries = dict(zip(employees['SAL'].unique(), count()))
employees['SAL'] = employees['SAL'].map(salaries)

corr_table = employees.corr().round(2)
print(corr_table, end='\n\n')
# corr_table.to_csv(corr_table_path)

crosstab(index=employees['left'], columns=employees['WA'])

