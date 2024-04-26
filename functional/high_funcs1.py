def map_user(func_obj: 'function', iterable) -> list:
    """Функция высшего порядка."""
    results = []
    for elem in iterable:
        results.append(func_obj(elem))
    return results


def encode(number: int) -> str:
    result = ''
    for digit in str(number):
        result += chr(int(digit) + 90)
    return result


# >>> map_user(encode, [1783, 1921, 2194, 3706])
# ['[ab]', '[c\\[', '\\[c^', ']aZ`']

# >>> map_user(
# ...     lambda n: 2**(3.141592*n), 
# ...     [1, 3, 4, 6, 7, 9]
# ... )
# [8.824973829062873, 687.290401016313, 6065.319801935086, 472368.0953291643, 4168636.078964149, 324654057.66609246]

# >>> map_user(
# ...     lambda n, pi=3.141592: 2**(pi*n),
# ...     [1, 2, 3/2, 4/3, 1/6]
# ... )
# [8.824973829062873, 77.88016308364465, 26.2162240037789, 18.236909160359236, 1.437536578882782]

