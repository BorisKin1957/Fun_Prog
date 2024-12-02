def print_best_and_worst_laureate(dic_items):
    new = {}
    for value in dic_items.values():
        new[value] = new.get(value, 0) + 1
    result = sorted(new.items(), key=lambda item: item[1], reverse=True)
    print(*result[0], sep=', ')
    print(*result[-1], sep=', ')




laureates = {'За лучший фильм': 'Все везде и сразу',
             'За лучшую музыку к фильму': 'На Западном фронте без перемен',
             'За лучший звук': 'Топ Ган: Мэверик',
             'За лучшие визуальные эффекты': 'Аватар: Путь воды',
             'За лучший дизайн костюмов': 'Топ Ган: Мэверик',
             'За лучшую операторскую работу': 'На Западном фронте без перемен',
             'За лучший монтаж': 'Все везде и сразу',
             'За лучший оригинальный сценарий': 'Все везде и сразу',
             'За лучший фильм на иностранном языке': 'Все везде и сразу', }

print_best_and_worst_laureate(laureates)

print()

laureates = {'Премия «Оскар» за лучшую мужскую роль': 'Tom Kruize'}

print_best_and_worst_laureate(laureates)