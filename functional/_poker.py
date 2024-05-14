# старшая карта
# (2, 4, 10, 14, 5)
# пара
# (5, 7, 10, 4, 5)
# две пары
# (4, 5, 6, 6, 5)
# сет
# (7, 7, 2, 14, 7)
# фулл-хаус
# (4, 5, 4, 4, 5)
# стрит
# (4, 5, 6, 7, 8)
# каре
# (5, 5, 5, 4, 5)

# переменные для аннотаций
Hand = tuple[int, int, int, int, int]

def poker_comb(hand: Hand) -> str:
    """Находит самую старшую комбинацию в переданном итерируемом объекте. Возвращает название комбинации."""
    unique_cards = set(hand)
    unique_len = len(unique_cards)
    
    if unique_len == 4:
        return 'пара'
    
    if unique_len == 3:
        max_repeats = max(hand.count(card) for card in unique_cards)
        if max_repeats == 2:
            return 'две пары'
        else:
            return 'сет'
    
    min_card = min(unique_cards)
    if sorted(hand) == list(range(min_card, min_card+5)):
        return 'стрит'
    
    if unique_len == 2:
        max_repeats = max(hand.count(card) for card in unique_cards)
        if max_repeats == 3:
            return 'фулл-хаус'
        else:
            return 'каре'
    
    return 'старшая карта'


# >>> poker_comb([2, 4, 6, 8, 10])
# 'старшая карта'
# >>>
# >>> poker_comb([2, 2, 6, 8, 10])
# 'пара'
# >>>
# >>> poker_comb([2, 2, 6, 6, 10])
# 'две пары'
# >>>
# >>> poker_comb([2, 2, 2, 6, 10])
# 'сет'
# >>>
# >>> poker_comb([2, 2, 2, 6, 6])
# 'фулл-хаус'
# >>>
# >>> poker_comb([2, 2, 2, 2, 6])
# 'каре'

