# while <условие_продолжения_цикла>:
#     <тело_цикла>
#     ...


text = 'python — самый лучший язык!'
i = 0

print('начало цикла')

while i < len(text):
    
    if text[i].isalpha():
        print(text[i], '— буква')
    
    elif text[i].isspace():
        print(text[i], '— пробел')
    
    elif text[i] in '.,:;!?\'\"-–—':
        print(text[i], '— знак препинания')
    
    i += 1

print('конец цикла')

