def filter_user(predicate: 'function', iterable) -> list:
    results = []
    for elem in iterable:
        if predicate(elem):
            results.append(elem)
    return results


char_digits = set('0123456789')
first_char =  char_digits | {'-'}

def is_intable(number: str) -> bool:
    return set(number[:2]) <= first_char and set(number[2:]) <= char_digits

>>> filter_user(is_intable, ['24', '-15', '2', '2 2', '14'])
['24', '-15', '2', '14']


# >>> filter_user(is_intable, ['24', '-15', '2', '2 2', '14'])
# ['24', '-15', '2', '14']

# >>> text = '''If one positional argument is provided, it should be an iterable. The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned.'''
# >>>
# >>> filter_user(lambda w: len(w) > 3, text.split())
# ['positional', 'argument', 'provided,', 'should', 'iterable.', 'largest', 'item', 'iterable', 'returned.', 'more', 'positional', 'arguments', 'provided,', 'largest', 'positional', 'arguments', 'returned.']

