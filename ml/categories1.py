from pandas import DataFrame, Categorical

from itertools import count



credit_scores = DataFrame({
    'имя': ['Иван', 'Сергей', 'Дмитрий', 'Артём', 'Георгий', 'Леонид', 'Игорь', 'Павел', 'Пётр', 'Кирилл'],
    'город': ['Москва', 'Москва', 'Санкт-Петербург', 'Нижний Новгород', 'Москва', 'Казань', 'Екатеринбург', 'Санкт-Петербург', 'Москва', 'Казань'],
    'сумма': [0.25, 1.5, 0.78, 32.5, 0.51, 2.83, 10.1, 12.0, 3.05, 29.3],
    'длительность': [6, 12, 6, 24, 4, 12, 6, 9, 6, 36],
    'процент': [0.27, 0.11, 0.36, 0.075, 0.20, 0.16, 0.09, 0.12, 0.35, 0.081],
    'рейтинг': ['высокий', 'низкий', 'средний', 'средний', 'очень высокий', 'низкий', 'средний', 'высокий', 'средний', 'средний'],
    'одобрение': ['одобрен', 'не одобрен', 'одобрен', 'одобрен', 'одобрен', 'не одобрен', 'одобрен', 'одобрен', 'одобрен', 'не одобрен'],
})

credit_scores_coded1 = credit_scores.iloc[:, :-1]

approved_codes = []
for v in credit_scores['одобрение'].values:
    if v == 'одобрен':
        approved_codes.append(1)
    else:
        approved_codes.append(0)

credit_scores_coded1['одобрение'] = approved_codes


credit_scores_coded2 = credit_scores.iloc[:, :-1]

approved_codes_dict = {
    'не одобрен': 0,
    'одобрен': 1
}
credit_scores_coded2['одобрение'] = [
    approved_codes_dict[v]
    for v in credit_scores['одобрение'].values 
]

credit_scores_coded3 = credit_scores.copy()
cities_codes = dict(zip(credit_scores['город'].unique(), count()))
credit_scores_coded3['город'] = credit_scores['город'].map(cities_codes)


credit_scores_coded4 = credit_scores.copy()
credit_scores_coded4['город'] = Categorical(credit_scores['город'])

