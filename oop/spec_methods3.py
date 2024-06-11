from random import choice, sample, randrange as rr
from string import ascii_lowercase as letters


class Telephone:
    def __init__(self, number: str):
        self.number = number
    
    def __call__(self, number_to_dial: str):
        print(f'{self.number} набирает {number_to_dial}:')
        while choice([0, 1, 1, 1, 1, 1]):
            input('говорите: ')
            print(self.get_phrase())
        print(f'{number_to_dial} прервал связь')
    
    @staticmethod
    def get_phrase() -> str:
        return ' '.join(
            ''.join(sample(letters, rr(3, 8)))
            for _ in range(rr(2, 6))
        )


me = Telephone('000-111-222')

# >>> me('333-444-555')
# 000-111-222 набирает 333-444-555:
# говорите: привет!
# zyctp hbvmaf hzu imkc qypmt
# 333-444-555 прервал связь
# >>>
# >>> me('333-444-555')
# 000-111-222 набирает 333-444-555:
# 333-444-555 прервал связь
# >>>
# >>> me('333-444-666')
# 000-111-222 набирает 333-444-666:
# говорите: привет, ты кто?
# bac ldaxg scqrp ecszn qvdgca
# говорите: меня зовут genndalf
# esdkzhl rbzk szvwnjl
# 333-444-666 прервал связь

