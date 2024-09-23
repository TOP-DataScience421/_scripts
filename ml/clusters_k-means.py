from matplotlib import (
    pyplot as plt,
    rcParams,
)
from numpy import array
from pandas import read_csv

from pathlib import Path
from random import uniform
from sys import path
from time import sleep


colors = [
    '#FF8C00',
    '#556B2F',
    '#4169E1',
]

rcParams['toolbar'] = 'None'
rcParams['font.size'] = 13
rcParams['axes.titlesize'] = 20

plt.ion()

fig = plt.figure(num='', figsize=(8,8))
axs = fig.add_subplot()


data = read_csv(Path(path[0]) / 'test_clusters.csv')
data.columns = ['x1', 'x2']

# количество кластеров и центроид
c = 3

# выбор равноудалённых центроид
centroids = [
    (data['x1'].min(), data['x2'].min()),
    (data['x1'].max(), data['x2'].max()),
    (data['x1'].mean(), data['x2'].mean()),
]

# выбор случайных центроид
centroids = [
    (uniform(data['x1'].min(), data['x1'].max()), uniform(data['x2'].min(), data['x2'].max())),
    (uniform(data['x1'].min(), data['x1'].max()), uniform(data['x2'].min(), data['x2'].max())),
    (uniform(data['x1'].min(), data['x1'].max()), uniform(data['x2'].min(), data['x2'].max())),
]

# выбор центроид из сегментированного распределения исходных данных
data_sort = data.copy().sort_values('x1')
p1 = int(len(data)/3)
p2 = p1 * 2
centroids = [
    (data_sort.iloc[:p1, 0].median(), data_sort.iloc[:p1, 1].median()),
    (data_sort.iloc[p1:p2, 0].median(), data_sort.iloc[p1:p2, 1].median()),
    (data_sort.iloc[p2:, 0].median(), data_sort.iloc[p2:, 1].median()),
]

# === визуализация ===
axs.clear()
axs.set(
    xlabel='x1', 
    ylabel='x2',
    title='исходные данные'
)
axs.scatter(data['x1'], data['x2'])
for k in range(c):
    axs.scatter(centroids[k][0], centroids[k][1], s=100, c='r', marker='^')
plt.draw()
plt.gcf().canvas.flush_events()
sleep(3)
# === визуализация ===

for _ in range(5):
    # пустые списки под будущие кластеры
    clusters = [[] for _ in range(c)]
    
    # для каждой точки (вектора) вычисляем расстояния до каждой центроиды
    for i in range(len(data)):
        distances = []
        for k in range(c):
            dx = data.iloc[i]['x1'] - centroids[k][0]
            dy = data.iloc[i]['x2'] - centroids[k][1]
            distances.append((dx**2 + dy**2)**0.5)
        # до какой центроиды расстояние минимально ...
        k_min = distances.index(min(distances))
        # ... в такой кластер добавлем точку (вектор)
        clusters[k_min].append((data.iloc[i]['x1'], data.iloc[i]['x2']))
    
    # вспомогательное преобразование в numpy.ndarray
    for k in range(c):
        clusters[k] = array(clusters[k])
    
    # === визуализация ===
    axs.clear()
    axs.set(
        xlabel='x1', 
        ylabel='x2',
        title='каждая точка отнесена к тому кластеру,\nрасстояние до центроиды которого меньше'
    )
    for k in range(c):
        if len(clusters[k]) > 0:
            axs.scatter(*clusters[k].T, c=colors[k])
        axs.scatter(*centroids[k], s=100, c=colors[k], marker='^')
    plt.draw()
    plt.gcf().canvas.flush_events()
    sleep(1)
    # === визуализация ===
    
    # перемещение центроид в геометрический центр получившихся кластеров
    for k in range(c):
        # на практике среднеарифметическое не используют
        if len(clusters[k]) > 0:
            centroids[k] = (clusters[k].T[0].mean(), clusters[k].T[1].mean())
        # а используют нахождение минимума производной от функции суммы квадратов внутрикластерных расстояний
    
    # === визуализация ===
    axs.clear()
    axs.set(
        xlabel='x1', 
        ylabel='x2',
        title='новые центроиды помещены в центр кластеров'
    )
    for k in range(c):
        if len(clusters[k]) > 0:
            axs.scatter(*clusters[k].T, c=colors[k])
        axs.scatter(*centroids[k], s=100, c=colors[k], marker='^')
    plt.draw()
    plt.gcf().canvas.flush_events()
    sleep(1)
    # === визуализация ===


plt.ioff()
plt.show()


