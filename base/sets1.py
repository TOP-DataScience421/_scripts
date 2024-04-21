from random import sample
from string import ascii_lowercase as lat_letters


empty_set = set()

cats = {'кот', 'кошка', 'котёнок'}

chars = set('The set type is mutable — the contents can be changed using methods like add() and remove().')

rand_words = {
    ''.join(sample(lat_letters, 2)) 
    for _ in range(100)
}


words = frozenset('The set type is mutable — the contents can be changed using methods like add() and remove().'.split())

