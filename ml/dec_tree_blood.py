from pandas import DataFrame
from scipy.io.arff import loadarff
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from pathlib import Path
from sys import path


data_path = Path(path[0]) / 'blood-transfusion-service-center.arff'
with open(data_path, encoding='utf-8') as filein:
    data_raw = loadarff(filein)


data = DataFrame(data_raw[0])

# >>> data['Class'].value_counts(normalize=True).round(2)
# Class
# b'1'    0.76
# b'2'    0.24
# Name: proportion, dtype: float64

data['Class'] = data['Class'].where(data['Class'] != b'1', 0)
data['Class'] = data['Class'].where(data['Class'] != b'2', 1)

data['Class'] = data['Class'].astype(int)

# >>> data.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 748 entries, 0 to 747
# Data columns (total 5 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   V1      748 non-null    float64
#  1   V2      748 non-null    float64
#  2   V3      748 non-null    float64
#  3   V4      748 non-null    float64
#  4   Class   748 non-null    int64
# dtypes: float64(4), int64(1)
# memory usage: 29.3 KB


x = data.iloc[:, :-1]
y = data['Class']

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

y_match = DataFrame({
    'actual': y_test, 
    'predicted': y_pred, 
    'match': y_test == y_pred
})

# >>> y_match['match'].value_counts(normalize=True).round(2)
# match
# True     0.73
# False    0.27
# Name: proportion, dtype: float64

# >>> confusion_matrix(y_test, y_pred)
# array([[124,  13],
#        [ 37,  13]])

