text = ''
print(repr(text), len(text))

# text = text + 'a'
text += 'a'
print(repr(text), len(text))
print("index of 'a'", text.index('a'))

text += 'b'
print(repr(text), len(text))
print("index of 'b'", text.index('b'))

text += 'a'
print(repr(text), len(text))
print("index of 'a'", text.index('a'))
