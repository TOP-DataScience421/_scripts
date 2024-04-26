def point(x: float, y: float, /, quarter: int):
    ...


# >>> point(2.5, 5, 1)

# >>> point(-3, 1.2, quarter=2)

# >>> point(x=8, y=1, quarter=1)
# TypeError: point() got some positional-only arguments passed as keyword arguments: 'x, y'

# >>> point(y=3.1, x=-4.1, quarter=2)
# TypeError: point() got some positional-only arguments passed as keyword arguments: 'x, y'

# >>> point(quarter=3, x=1, y=-2)
# TypeError: point() got some positional-only arguments passed as keyword arguments: 'x, y'

# >>> point(quarter=3, y=-2, x=3.1)
# TypeError: point() got some positional-only arguments passed as keyword arguments: 'x, y'

