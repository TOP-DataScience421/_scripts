from matplotlib import pyplot as plt
from matplotlib import rcParams
from pandas import read_csv

from pathlib import Path
from sys import path


rcParams['toolbar'] = 'None'
rcParams['font.size'] = 14
rcParams['axes.titlesize'] = 18


data_path = Path(path[0]) / 'boston.csv'
boston = read_csv(data_path, comment='#')


fig, axs = plt.subplots(2, 3)

axs[0][0].scatter(boston['RM'], boston['MEDV'])
axs[0][0].set_title('RM')

axs[0][1].scatter(boston['LSTAT'], boston['MEDV'])
axs[0][1].set_title('LSTAT')

axs[1][0].scatter(boston['TAX'], boston['MEDV'])
axs[1][0].set_title('TAX')

axs[1][1].scatter(boston['INDUS'], boston['MEDV'])
axs[1][1].set_title('INDUS')

axs[1][2].scatter(boston['PTRATIO'], boston['MEDV'])
axs[1][2].set_title('PTRATIO')

plt.show()

