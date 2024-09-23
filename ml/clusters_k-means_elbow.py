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
    '#8B4513',
    '#DEB887',
    '#008000',
    '#ADFF2F',
    '#483D8B',
    '#87CEEB',
    '#700280',
    '#DDA0DD',
]

rcParams['toolbar'] = 'None'
rcParams['font.size'] = 13
rcParams['axes.titlesize'] = 20

plt.ion()

fig = plt.figure(num='', figsize=(17,8))
axs = fig.subplots(1, 2)


data = read_csv(Path(path[0]) / 'test_clusters.csv')
data.columns = ['x1', 'x2']


# суммы внутрикластерных расстояний
wcsd = []

for c in range(1, 8):
    # c — количество кластеров и центроид
    
    # выбор случайных центроид
    centroids = [
        (
            uniform(data['x1'].min(), data['x1'].max()), 
            uniform(data['x2'].min(), data['x2'].max())
        )
        for _ in range(c)
    ]
    
    # === визуализация ===
    axs[0].clear()
    axs[0].set(
        xlabel='x1', 
        ylabel='x2',
        title='исходные данные'
    )
    axs[0].scatter(data['x1'], data['x2'])
    for k in range(c):
        axs[0].scatter(centroids[k][0], centroids[k][1], s=100, c='r', marker='^')
    plt.draw()
    plt.gcf().canvas.flush_events()
    sleep(3)
    # === визуализация ===
    
    for _ in range(10):
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
        axs[0].clear()
        axs[0].set(
            xlabel='x1', 
            ylabel='x2',
            title='каждая точка отнесена к тому кластеру,\nрасстояние до центроиды которого меньше'
        )
        for k in range(c):
            if len(clusters[k]) > 0:
                axs[0].scatter(*clusters[k].T, c=colors[k])
            axs[0].scatter(*centroids[k], s=100, c=colors[k], marker='^')
        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(0.5)
        # === визуализация ===
        
        # перемещение центроид в геометрический центр получившихся кластеров
        for k in range(c):
            if len(clusters[k]) > 0:
                centroids[k] = (clusters[k].T[0].mean(), clusters[k].T[1].mean())
        
        # === визуализация ===
        axs[0].clear()
        axs[0].set(
            xlabel='x1', 
            ylabel='x2',
            title='новые центроиды помещены в центр кластеров'
        )
        for k in range(c):
            if len(clusters[k]) > 0:
                axs[0].scatter(*clusters[k].T, c=colors[k])
            axs[0].scatter(*centroids[k], s=100, c=colors[k], marker='^')
        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(0.5)
        # === визуализация ===
    
    # расчёт суммы внутрикластерных расстояний для всех кластеров для текущего количества кластеров
    total = 0
    for k in range(c):
        for point in clusters[k]:
            dx = point[0] - centroids[k][0]
            dy = point[1] - centroids[k][1]
            total += (dx**2 + dy**2)**0.5
    wcsd.append(total)
    
    # === визуализация ===
    axs[1].clear()
    axs[1].set(
        xlabel='количество кластеров', 
        ylabel='сумма внутрикластерных расстояний'
    )
    axs[1].plot(range(1, c+1), wcsd, '.-r', markersize=10)
    plt.draw()
    plt.gcf().canvas.flush_events()
    # === визуализация ===
    
    # прекращение увеличения количесва кластеров с уменьшением разности сумм внутрикластерных расстояний
    subs = array([
        wcsd[j] - wcsd[j-1]
        for j in range(1, c)
    ])
    if len(subs) > 0:
        subs = subs / subs[0]
    #     if subs[-1] < 0.15:
    #         break


plt.ioff()
plt.show()


