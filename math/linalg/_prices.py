from numpy import loadtxt, dot

from pathlib import Path
from sys import path


script_dir = Path(path[0])

prices = loadtxt(script_dir / 'prices.data')
amounts = loadtxt(script_dir / 'amounts.data', dtype=int)

total_by_product = prices * amounts
total = dot(prices, amounts)

print(
    '\n'.join(
        f'товар {i}: {t:,.2f} ₽'
        for i, t in enumerate(total_by_product, 1)
    ),
    f'\nитого: {total:,.2f} ₽'
)

