from time import perf_counter

exp_prefixes = {
    '': 0,
    'м': 3,
    'мк': 6,
    'н': 9,
}


def timer(exp_prefix: str) -> 'function':
    exp = exp_prefixes.get(exp_prefix, 0)
    def decorator(func_obj: 'function') -> 'function':
        def wrapper(*args, **kwargs):
            start = perf_counter()
            result = func_obj(*args, **kwargs)
            end = perf_counter()
            elapsed = (end - start) * 10**exp
            print(f'вызов {func_obj.__name__}() занял {elapsed:.{9-exp}f} {exp_prefix}c')
            return result
        return wrapper
    return decorator



def list_to_set(iterable: list) -> set:
    return set(iterable)

list_to_set = timer('мк')(list_to_set)


@timer('мк')
def list_unique_list(iterable: list) -> list:
    result = []
    for elem in iterable:
        if elem not in result:
            result.append(elem)
    return result


from random import randrange

N = 10**4

test_data = [randrange(-99, 100) for _ in range(N)]

list_to_set(test_data)

list_unique_list(test_data)

