# number = input('число: ')
# 
# if number.isdigit():
#     number = int(number)
#     print(number + 10)
# else:
#     print('используйте только цифры')


try:
    number = int(input('число: '))
except ValueError:
    print('используйте только цифры')
else:
    print(number + 10)


# число: 12
# 22

# число: 1 2
# используйте только цифры
