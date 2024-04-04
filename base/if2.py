number = int(input('введите число: '))

if number % 2 == 0:
    print('чётное')
else:
    print('нечётное')


# введите число: 10
# чётное

# введите число: 33
# нечётное

# введите число: -16
# чётное

# введите число: 9g9
# ValueError: invalid literal for int() with base 10: '9g9'
