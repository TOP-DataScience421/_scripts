from matplotlib import pyplot as plt
from pandas import read_csv

from datetime import timedelta as td
from pathlib import Path
from sys import path


data = read_csv(
    Path(path[0]) / 'passengers.csv',
    index_col='month',
    parse_dates=True,
)
data_year = data.resample('YS').mean()
ma = data.rolling(window=12).mean()



fig = plt.figure()
axs = fig.subplots()

axs.plot(data)
axs.plot(ma, c='r')

plt.show()



