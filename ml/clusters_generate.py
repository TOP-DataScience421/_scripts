from matplotlib import pyplot as plt
from numpy import array, savetxt

from pathlib import Path
from random import randrange as rr, uniform, shuffle
from sys import path


output_path = Path(path[0]) / 'test_clusters_mixed.csv'


cluster1, cluster2, cluster3 = [], [], []

for _ in range(rr(20, 30)):
    cluster1.append((uniform(-2, 0), uniform(1.5, 4)))

for _ in range(rr(20, 30)):
    cluster2.append((uniform(-1, 2.5), uniform(2.5, 4.5)))

for _ in range(rr(20, 30)):
    cluster3.append((uniform(0.5, 3), uniform(1, 3)))


data = cluster1 + cluster2 + cluster3
shuffle(data)
data = array(data)

savetxt(output_path, data, fmt='%.1f', delimiter=',')

plt.scatter(data.T[0], data.T[1])
plt.show()
