from itertools import permutations, combinations


strings = [
    'A',
    'AB',
    'ABC',
    'ABCD',
]

for s in strings:
    perms = list(permutations(s, len(s)))
    print(f'\n\nперестановок: {len(perms)}')
    for p in perms:
        print(*p, sep='', end='  ')


students = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
combs = list(combinations(students, 3))

# >>> len(combs)
# 2300

