class Title(str):
    def __new__(cls, value: str):
        if not isinstance(value, str):
            raise ValueError
        return super().__new__(cls, value.upper())


h1 = Title('очень классный заголовок')

# >>> h1
# 'ОЧЕНЬ КЛАССНЫЙ ЗАГОЛОВОК'

# >>> h1.__class__
# <class '__main__.Title'>
