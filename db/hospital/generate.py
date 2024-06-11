from datetime import date, timedelta as td
from random import randrange as rr, uniform, choice
from sys import path

path.insert(0, r'D:\G-Doc\TOP Academy\Python web\! Задачи\9. Стандартная библиотека')

import generate_person as person

person.load_data()


prob_10 = [False] + [True]*9

departments = [
    ("Отделение общей терапии",),
    ("Неврологическое отделение",),
    ("Кардиологическое отделение",),
    ("Отделение функциональной диагностики",),
    ("Реанимация и интенсивная терапия",),
    ("Токсикологическое отделение",),
    ("Физиотерапевтическое отделение",),
]
sponsors = [
    ("Детский паллиатив",), 
    ("Обнимая небо",), 
    ("Фонд имени Анжелы Вавиловой",),
    ("Защити жизнь",), 
    ("Близко к сердцу",), 
    ("София",), 
    ("ДоброДомик",), 
    ("Апельсин",), 
    ("Преодолей-ка",), 
    ("Близкие другие",), 
    ("Галчонок",), 
    ("Перспективы",), 
    ("Жизненный путь",),
]
specializations = [
    ("Анестезиолог",),
    ("Гастроэнтеролог",),
    ("Дерматолог",),
    ("Диетолог",),
    ("Иммунолог",),
    ("Кардиолог",),
    ("Невролог",),
    ("Нарколог",),
    ("Онколог",),
    ("Ортопед",),
    ("Оториноларинголог",),
    ("Офтальмолог",),
    ("Реаниматолог",),
    ("Ревматолог",),
    ("Стоматолог",),
    ("Терапевт",),
    ("Травматолог",),
    ("Уролог",),
    ("Хирург",),
    ("Эндокринолог",),
]

wards = []
for fk, dep in enumerate(departments, 1):
    for n in range(1, rr(3, 6)):
        ward = ''.join(
            w[0].upper() 
            for w in dep[0].split() 
            if len(w) > 1
        )
        wards.append((fk, f'{ward}-{n}'))

# print(*wards, sep=',\n')


donations = []
for _ in range(50):
    year, month, day = person.rand_date(years_period=10)
    donations.append((
        rr(1, 14),
        rr(1, 8),
        f'{year}-{month:0>2}-{day:0>2}',
        float(rr(120, 795)*1000),
    ))

# print(*donations, sep=',\n')


doctors = []
for _ in range(70):
    pers = person.generate_person()
    premium = float(rr(100, 530)*100) if choice(prob_10) else 0.0
    doctors.append((
        rr(1, 8),
        pers['фамилия'],
        pers['имя'],
        pers['отчество'],
        float(rr(340, 780)*100),
        premium,
    ))

# print(*doctors, sep=',\n')


doctors_specs = []
for _ in range(50):
    spec_cnt = 1 if choice(prob_10) else 2
    for _ in range(spec_cnt):
        doctors_specs.append((
            rr(1, 71),
            rr(1, 21),
        ))

# print(*doctors_specs, sep=',\n')


vacations = []
for _ in range(250):
    start_date = date(*person.rand_date(years_period=7))
    end_date = start_date + td(days=rr(5, 22))
    vacations.append((
        rr(1, 71),
        f'{start_date:%Y-%m-%d}',
        f'{end_date:%Y-%m-%d}',
    ))

# print(*vacations, sep=',\n')

