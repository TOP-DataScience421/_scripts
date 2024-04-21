fruit_colors = {
    'яблоко': 'зелёный',
    'банан': 'жёлтый',
    'апельсин': 'оранжевый',
    'слива': 'красный',
    'груша': 'зелёный',
}

# >>> len(fruits_colors)
# 5
# >>>
# >>> fruits_colors['банан']
# 'жёлтый'
# >>>
# >>> fruit_colors['персик']
# KeyError: 'персик'
# >>>
# >>> fruit_colors[0]
# KeyError: 0


# >>> id(fruits_colors)
# 2201096320576
# >>>
# >>> fruits_colors['слива'] = 'тёмно-фиолетовый'
# >>> fruits_colors['слива']
# 'тёмно-фиолетовый'
# >>>
# >>> id(fruits_colors)
# 2201096320576


# >>> for key in fruits_colors:
# ...     print(key)
# ...
# яблоко
# банан
# апельсин
# слива
# груша
# >>>
# >>> for key in fruits_colors.keys():
# ...     print(key)
# ...
# яблоко
# банан
# апельсин
# слива
# груша
# >>>
# >>> for value in fruits_colors.values():
# ...     print(value)
# ...
# зелёный
# жёлтый
# оранжевый
# тёмно-фиолетовый
# зелёный
# >>>
# >>> for item in fruits_colors.items():
# ...     print(item)
# ...
# ('яблоко', 'зелёный')
# ('банан', 'жёлтый')
# ('апельсин', 'оранжевый')
# ('слива', 'тёмно-фиолетовый')
# ('груша', 'зелёный')
# >>>
# >>> for key, value in fruits_colors.items():
# ...     print(f'{key=!r}\t{value=!r}')
# ...
# key='яблоко'    value='зелёный'
# key='банан'     value='жёлтый'
# key='апельсин'  value='оранжевый'
# key='слива'     value='тёмно-фиолетовый'
# key='груша'     value='зелёный'
# >>>


numbers_evenity = {
    1: 'простое', 
    2: 'не простое', 
    3: 'простое', 
    4: 'не простое', 
    5: 'простое', 
    6: 'не простое'
}

# >>> numbers_evenity[7]
# KeyError: 7
# >>>
# >>> numbers_evenity.get(7)
# >>> numbers_evenity.get(7, '')
# ''
# >>>
# >>> numbers_evenity.get(5)
# 'простое'
# >>> numbers_evenity.get(5, '')
# 'простое'
# >>>
# >>> numbers_evenity.setdefault(5)
# 'простое'
# >>>
# >>> numbers_evenity
# {1: 'простое', 2: 'не простое', 3: 'простое', 4: 'не простое', 5: 'простое', 6: 'не простое'}
# >>>
# >>> numbers_evenity.setdefault(7)
# >>>
# >>> numbers_evenity
# {1: 'простое', 2: 'не простое', 3: 'простое', 4: 'не простое', 5: 'простое', 6: 'не простое', 7: None}

