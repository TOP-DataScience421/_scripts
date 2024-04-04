n1 = float(input('число 1: '))
n2 = float(input('число 2: '))

# число 1: 8
# число 2: 4
# 8.0 / 4.0 = 2.0

# print(n1, '/', n2, '=', n1 / n2)

# print(str(n1) + ' / ' + str(n2) + ' = ' + str(n1 / n2))

print(f'{n1:_>6} / {n2:_<6} = {n1 / n2:.2f}')

