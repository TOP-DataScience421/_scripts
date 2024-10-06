from pandas import read_csv
from statsmodels.tsa.stattools import adfuller, kpss

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

alpha = 0.05

# тест Дики-Фуллера:
# H0 - ряд нестационарный
# H1 - ряд стационарный

passengers_adfuller_result = adfuller(passengers)
births_adfuller_result = adfuller(births)

# тест KPSS:
# H0 - ряд стационарный
# H1 - ряд нестационарный

passengers_kpss_result = kpss(passengers)
births_kpss_result = kpss(births)


# >>> passengers_adfuller_result[1]
# np.float64(0.991880243437641)
# p-value > уровень значимости, H0 не может быть отвергнута, ряд нестационарный

# >>> passengers_kpss_result[1]
# np.float64(0.01)
# p-value < уровень значимости, H0 отвергается, ряд нестационарный

# результаты статистических тестов совпадают, ряд точно стационарный


# >>> births_adfuller_result[1]
# np.float64(5.2434129901498554e-05)
# p-value < уровень значимости, H0 отвергается, ряд стационарный

# >>> births_kpss_result[1]
# np.float64(0.01)
# p-value < уровень значимости, H0 отвергается, ряд нестационарный

# результаты статистических тестов не совпадают, вероятно, требуется предпринять дополнительные действия с временным рядом: отсечка, расширение, дифференцирование, фильтрация, ...

