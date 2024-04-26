def gcd(num1: int, num2: int) -> int:
    print(f'{num1=} {num2=}')
    if num2:
        return gcd(num2, num1 % num2)
    else:
        return num1


# >>> gcd(15, 12)
# num1=15 num2=12
# num1=12 num2=3
# num1=3 num2=0
# 3

# >>> gcd(12, 6)
# num1=12 num2=6
# num1=6 num2=0
# 6

# >>> gcd(17, 3)
# num1=17 num2=3
# num1=3 num2=2
# num1=2 num2=1
# num1=1 num2=0
# 1

