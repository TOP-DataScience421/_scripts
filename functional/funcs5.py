punctuation = '.,:;!?-–—\'\"()'

def translator(text: str, **words_translation: str) -> str:
    words = [
        word_cl.lower() 
        for word in text.split() 
        if (word_cl := word.strip(punctuation))
    ]
    return ' '.join(
        words_translation[word]
        for word in words
    )


print(translator(
    'the dog catched a cat',
    the='',
    dog='собака',
    catched='поймал',
    a='',
    cat='кот',
))


from sys import argv


def args_parser(*args: str) -> dict:
    kwargs = {}
    value = False
    prev_arg = None
    for arg in args:
        if arg.startswith('-'):
            if value:
                kwargs[prev_arg.strip('-')] = True
                prev_arg = arg
            else:
                prev_arg = arg
                value = True
        else:
            if value:
                kwargs[prev_arg.strip('-')] = arg
                value = False
    if value:
        kwargs[prev_arg.strip('-')] = True
    return kwargs


def args_handler(**parameters: str | bool) -> None:
    print(type(parameters), parameters, sep='\n')


args_handler(**args_parser(*argv[1:]))

#  > python funcs5.py -l 10 --store_true
# <class 'dict'>
# {'l': '10', 'store_true': True}

#  > python funcs5.py --parse --mode
# <class 'dict'>
# {'parse': True, 'mode': True}

#  > python funcs5.py --parse --mode 5
# <class 'dict'>
# {'parse': True, 'mode': '5'}

