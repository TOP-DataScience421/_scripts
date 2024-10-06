from matplotlib import pyplot as plt
from pandas import (
    concat,
    DataFrame,
    read_csv,
)

from datetime import timedelta as td
from pathlib import Path
from sys import path


births = read_csv(
    Path(path[0]) / 'births.csv',
    index_col='date',
    parse_dates=True,
)

# predicted_t+1 = alpha * actual_t + (1 - alpha) * predicted_t

alpha = 0.2

index_t_plus_1 = births.iloc[-1:].index + td(days=1)
births = concat([births, DataFrame(index=index_t_plus_1)])

births['births_exp'] = [float('nan')] * len(births)

births.iloc[1, 1] = births.iloc[0, 0]

for t in range(2, len(births)):
    predicted = alpha * births.iloc[t-1, 0] + (1 - alpha) * births.iloc[t-1, 1]
    births.iloc[t, 1] = predicted


fig = plt.figure()
axs = fig.subplots()

axs.plot(births['births'])
axs.plot(births['births_exp'], color='orange')

plt.show()

