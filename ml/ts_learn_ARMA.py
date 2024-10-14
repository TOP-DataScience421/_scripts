from matplotlib import pyplot as plt
from pandas import read_csv
from statsmodels.tsa.arima.model import ARIMA

from datetime import timedelta as td, date
from pathlib import Path
from sys import path
from time import sleep
from warnings import simplefilter

simplefilter(action='ignore', category=Warning)


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
births_train = births.loc[:date(1959, 10, 31)]
births_test = births.loc[date(1959, 11, 1):]


plt.ion()

fig = plt.figure(
    figsize=(10, 3),
)
axs = fig.subplots()

for p in range(61, 62):
    
    # алгоритмическая модель ARMA(p, q)
    model = ARIMA(births_train, order=(p, 0, 1), enforce_stationarity=False)
    model_result = model.fit()
    
    left = births_train.index[-1] + td(days=1)
    right = left + td(days=61)
    
    births_pred = model_result.predict(left, right)
    
    axs.clear()
    axs.set(
        title=f'{p = }',
    )
    axs.plot(births_train, c='black')
    axs.plot(births_test, c='green')
    axs.plot(births_pred, c='red')
    
    plt.draw()
    plt.gcf().canvas.flush_events()
    
    sleep(0.1)

plt.ioff()
plt.show()

