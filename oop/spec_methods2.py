class Color:
    colors_hex = {
        'красный': 'ff0000',
        'зелёный': '00ff00',
        'синий': '0000ff',
    }
    
    def __init__(self, color: str):
        try:
            int(color, 16)
        except ValueError:
            self.color = self.colors_hex.get(color, '000000')
        else:
            self.color = color.lower()
    
    # self == other
    def __eq__(self, other):
        if isinstance(other, Color):
            return self.color == other.color
        elif isinstance(other, str):
            return self.color == other
        else:
            raise TypeError(f"{self.__class__.__name__!r} can be compared only with same and 'str' classes")


red1 = Color('красный')
red2 = Color('ff0000')

# red1 == red2 --> red1.__eq__(red2)

# >>> red1 == red2
# True

green = Color('зелёный')

# >>> red1 == green
# False
# >>>
# >>> green == '00ff00'
# True
# >>>
# >>> green == '00fa10'
# False

# >>> red1 != red2
# False
# >>>
# >>> red1 != green
# True

