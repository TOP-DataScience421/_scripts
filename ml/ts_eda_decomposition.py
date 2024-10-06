from matplotlib import pyplot as plt
from pandas import (
    DataFrame,
    read_csv,
)
from statsmodels.tsa.seasonal import seasonal_decompose

from datetime import timedelta as td
from pathlib import Path
from sys import path


passengers = read_csv(
    Path(path[0]) / 'passengers.csv',
    index_col='month',
    parse_dates=True,
)
births = read_csv(
    Path(path[0]) / 'births.csv',
    index_col='date',
    parse_dates=True,
)

window_width = 12

passengers_ma = passengers.rolling(window_width).mean()

passengers_season = passengers - passengers_ma
for i in range(window_width, len(passengers) - window_width):
    subgroup = passengers_season.iloc[i::window_width]
    passengers_season.iloc[i] = subgroup.mean()

passengers_residuals = passengers - passengers_ma - passengers_season


fig = plt.figure(
    figsize=(7, 10),
    layout='constrained',
)
axs = fig.subplots(4, 1)

left = passengers.index[0] - td(days=60)
right = passengers.index[-1] + td(days=60)

axs[0].plot(passengers)
axs[0].set(
    xlim=(left, right),
    ylabel='passengers',
)
axs[1].plot(passengers_ma)
axs[1].set(
    xlim=(left, right),
    ylabel='trend',
)
axs[2].plot(passengers_season)
axs[2].set(
    xlim=(left, right),
    ylabel='seasonality',
)
axs[3].scatter(passengers_residuals.index, passengers_residuals, s=25)
axs[3].set(
    xlim=(left, right),
    ylabel='residuals',
)

births_decompose = seasonal_decompose(births, period=21)
fig2 = births_decompose.plot()

fig2.set_size_inches(7, 10)

plt.show()

