PROMPT = '\n > '

print('\nКОМАНДНАЯ СТРОКА 1')

command = input(PROMPT)
# условие продолжения цикла
while command in ('exit', 'quit'):
    
    if command == 'line':
        print('—'*40)
    
    elif command == 'square':
        print('—'*10)
        for _ in range(5):
            print('|', ' '*8, '|', sep='')
        print('—'*10)
    
    else:
        print('unknown command')
    
    command = input(PROMPT)

print('\nКОМАНДНАЯ СТРОКА 2')

while True:
    
    command = input(PROMPT)
    
    # условие прекращения цикла
    if command in ('exit', 'quit'):
        break
    
    elif command == 'line':
        print('—'*40)
    
    elif command == 'square':
        print('—'*10)
        for _ in range(5):
            print('|', ' '*8, '|', sep='')
        print('—'*10)
    
    else:
        print('unknown command')


# КОМАНДНАЯ СТРОКА 1
# 
#  > abracadabra
# unknown command
# 
#  > line
# ————————————————————————————————————————
# 
#  > square
# ——————————
# |        |
# |        |
# |        |
# |        |
# |        |
# ——————————
# 
#  > exit
# 
# КОМАНДНАЯ СТРОКА 2
# 
#  > square
# ——————————
# |        |
# |        |
# |        |
# |        |
# |        |
# ——————————
# 
#  > line
# ————————————————————————————————————————
# 
#  > quit

