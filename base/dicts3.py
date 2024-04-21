char_codes = {
    chr(code): code
    for code in range(ord('a'), ord('z')+1)
}

# >>> char_codes
# {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}

code = int(input('введите код буквы: '))
for key, value in char_codes.items():
    if value == code:
        print(key)
        break
else:
    print('код не найден')


code_chars = {v: k for k, v in char_codes.items()}
print(code_chars[code])


# введите код буквы: 100
# d
# d

# введите код буквы: 200
# код не найден
# код не найден

