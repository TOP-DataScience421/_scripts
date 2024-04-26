def fibonacci(N: int | None = None):
    if N is None:
        N = float('inf')
    n1, n2 = 1, 1
    if N > 0:
        yield n1
    if N > 1:
        yield n2
    cnt = 2
    while cnt < N:
        n1, n2 = n2, n1 + n2
        yield n2
        cnt += 1


# >>> list(fibonacci(10))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
# >>> 
# >>> list(fibonacci(2))
# [1, 1]
# >>> 
# >>> list(fibonacci(1))
# [1]
# >>> 
# >>> list(fibonacci(0))
# []

