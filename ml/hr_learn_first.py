from pandas import (
    read_csv,
    Categorical,
    crosstab,
    DataFrame,
)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix,
    recall_score,
    precision_score,
    accuracy_score,
)

from itertools import count
from pathlib import Path
from sys import path


datafile_path = Path(path[0]) / 'HR.csv'


employees = read_csv(datafile_path, comment='#')

employees.columns = ('SLVL', 'LE', 'NP', 'AMH', 'TSC', 'WA', 'left', 'PROM5', 'DEP', 'SAL')
employees['DEP'] = Categorical(
    employees['DEP']
).codes
employees['SAL'] = Categorical(
    employees['SAL'],
    ['low', 'medium', 'high'],
    ordered=True,
).codes

x = employees.loc[:, ('SLVL', 'LE', 'NP', 'AMH', 'TSC', 'WA', 'PROM5', 'DEP', 'SAL')]
y = employees['left']

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=1/3,
    random_state=3
)

for lbl in ('SLVL', 'LE', 'NP', 'AMH', 'TSC'):
    x_train[lbl] = (x_train[lbl] - x_train[lbl].mean()) / x_train[lbl].std()


model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

cm = DataFrame(cm, columns=['остался', 'ушёл'], index=['остался', 'ушёл'])
print(cm)

#          остался  ушёл
# остался        0  3817
# ушёл           0  1183


# условные примеры для понимания смысла метрик
# 
# n_test = 10
#                       прогноз
#                |—————————|————————|
#                | остался |  ушёл  |
#      |—————————|—————————|————————|
#      | остался | 7 (TN)  | 1 (FP) | 
# факт |—————————|—————————|————————|
#      |  ушёл   | 1 (FN)  | 1 (TP) |
#      |—————————|—————————|————————|
#                     -        +     
#
#                  TN + TP            7 + 1    
# acccuracy = ————————————————— = ————————————— = 0.8
#             TN + FN + TP + FP   7 + 1 + 1 + 1
#
#               TP        1
# precision = ——————— = ————— = 0.5
#             TP + FP   1 + 1
#
#            TP        1
# recall = ——————— = ————— = 0.5
#          TP + FN   1 + 1
# 
#      2 * precision * recall   2 * 0.5 * 0.5
# f1 = —————————————————————— = ————————————— = 0.5
#        precision + recall       0.5 + 0.5



# n_test = 100
#                       прогноз
#                |—————————|————————|
#                | остался |  ушёл  |
#      |—————————|—————————|————————|
#      | остался | 80 (TN) | 2 (FP) | 
# факт |—————————|—————————|————————|
#      |  ушёл   | 13 (FN) | 5 (TP) |
#      |—————————|—————————|————————|
#                     -         +    
#
#                  TN + TP             80 + 5    
# acccuracy = ————————————————— = ——————————————— = 0.85
#             TN + FN + TP + FP   80 + 13 + 5 + 2
#
#               TP        5
# precision = ——————— = ————— = 0.71
#             TP + FP   5 + 2
#
#            TP        5
# recall = ——————— = —————— = 0.385
#          TP + FN   5 + 13
# 
#      2 * precision * recall   2 * 0.71 * 0.385
# f1 = —————————————————————— = ———————————————— = 0.499
#        precision + recall       0.71 + 0.385

