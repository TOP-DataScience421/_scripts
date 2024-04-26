data1 = [
    (1, 2, 3),
    (4, 5, 6),
]
data2 = [
    [
        (1, 2, 3),
        (4, 5, 6),
    ],
    [
        (7, 8, 9),
        (10, 11, 12),
    ],
]
data3 = [
    (
        [
            {1, 2, 3},
            {4, 5, 6},
        ],
        [
            {7, 8, 9},
            {10, 11, 12},
        ],
    ),
    (
        [
            {13, 14, 15},
            {16, 17, 18},
        ],
        [
            {19, 20, 21},
            {22, 23, 24},
        ],
    ),
]


from collections.abc import Iterable


def flatten(data: Iterable) -> list[int]:
    # breakpoint()
    result = []
    for elem in data:
        if isinstance(elem, Iterable):
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result


# >>> flatten(data1)
# [1, 2, 3, 4, 5, 6]

# >>> flatten(data2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# >>> flatten(data3)
# [1, 2, 3, 4, 5, 6, 8, 9, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 24, 22, 23]

