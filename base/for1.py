# for <переменная_цикла> in <выражение_возвращающее_итерируемый_объект>:
#     <тело_цикла>
#     ...

text = 'python — самый лучший язык!'

print('начало цикла')

for char in text:
    
    if char.isalpha():
        print(char, '— буква')
    
    elif char.isspace():
        print(char, '— пробел')
    
    elif char in '.,:;!?\'\"-–—':
        print(char, '— знак препинания')

print('конец цикла')

