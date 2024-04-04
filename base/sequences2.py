word = 'python'

i = 0
print('элемент по индексу', i, repr(word[i]))
i += 1
print('элемент по индексу', i, repr(word[i]))
i += 1
print('элемент по индексу', i, repr(word[i]))
i += 1
print('элемент по индексу', i, repr(word[i]))
i += 1
print('элемент по индексу', i, repr(word[i]))
i += 1
print('элемент по индексу', i, repr(word[i]), end='\n\n')

# >>> word[6]
# IndexError: string index out of range

i = -1
print('элемент по индексу', i, repr(word[i]))
i -= 1
print('элемент по индексу', i, repr(word[i]))
i -= 1
print('элемент по индексу', i, repr(word[i]))
i -= 1
print('элемент по индексу', i, repr(word[i]))
i -= 1
print('элемент по индексу', i, repr(word[i]))
i -= 1
print('элемент по индексу', i, repr(word[i]), end='\n\n')

# >>> word[-7]
# IndexError: string index out of range

