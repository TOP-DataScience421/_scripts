numbers1 = list(range(10, 100, 10))
numbers2 = list(range(10, 100, 10))
numbers3 = list(range(10, 100, 10))

i = 0
for n in numbers1:
    if not n % 3:
        numbers1[i] = 3
    i += 1

for i in range(len(numbers2)):
    if not numbers2[i] % 3:
        numbers2[i] = 3

for i, n in enumerate(numbers3):
    if not n % 3:
        numbers3[i] = 3

print(numbers1, numbers2, numbers3, sep='\n')

