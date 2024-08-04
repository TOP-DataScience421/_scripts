from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import arange, linspace
from scipy.stats import norm
from time import sleep

rcParams['toolbar'] = 'None'
rcParams['font.size'] = 14
rcParams['axes.titlesize'] = 18

plt.ion()

fig = plt.figure(
    num='', 
    figsize=(8, 6)
)
axs = fig.add_subplot()

N = 100
x = arange(0, N)

for d in linspace(0.99, 0.01, N):
    y = norm.rvs(size=N, scale=d)
    
    axs.clear()
    axs.set(
        title=f'D = {d:.2f}',
        xticks=[],
        ylim=(-3, 3),
    )
    axs.scatter(x, y)
    plt.draw()
    plt.gcf().canvas.flush_events()
    
    sleep(0.05)

plt.ioff()
plt.show()

