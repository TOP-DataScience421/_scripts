# cubes = list(n**3 for n in range(2, 10))

# то же самое
cubes = [n**3 for n in range(2, 10)]
print(type(cubes), cubes, end='\n\n')

weights = {
    'Иван': 72.5,
    'Артём': 81.1,
    'Сергей': 76.9,
}
weights_normalized = {
    name: weight / 75
    for name, weight in weights.items()
}
print(type(weights_normalized), weights_normalized, end='\n\n')

text = '''The Python installers for the Windows platform usually include the entire standard library and often also include many additional components. For Unix-like operating systems Python is normally provided as a collection of packages, so it may be necessary to use the packaging tools provided with the operating system to obtain some or all of the optional components.'''
long_words = {w.lower() for w in text.split() if len(w) > 3}
print(type(long_words), long_words, end='\n\n')


# <class 'list'> [8, 27, 64, 125, 216, 343, 512, 729]
# 
# <class 'dict'> {'Иван': 0.9666666666666667, 'Артём': 1.0813333333333333, 'Сергей': 1.0253333333333334}
# 
# <class 'set'> {'include', 'components.', 'unix-like', 'usually', 'optional', 'installers', 'systems', 'collection', 'additional', 'many', 'some', 'also', 'standard', 'windows', 'operating', 'normally', 'packaging', 'obtain', 'entire', 'provided', 'packages,', 'library', 'necessary', 'with', 'python', 'system', 'often', 'platform', 'tools'}

