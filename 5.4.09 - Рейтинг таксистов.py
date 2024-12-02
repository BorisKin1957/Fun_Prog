def print_order_rating(names):
    new, average = {}, {}
    for name in names:
        new[name[0]] = new.get(name[0], []) + [name[1]]
    for key, value in new.items():
        average[key] = sum(value) / len(value)
    result = sorted(average.items(), key=lambda x: (-x[1], x[0].lower()))
    for key, value in result:
        print(key, value)


drivers = [
    ('Джек', 2),
    ('Джек', 3),
    ('Билл', 5),
    ('Билл', 4),
    ('Билл', 4),
    ('Билл', 3),
]
print_order_rating(drivers)

print()

drivers = [
    ('Зина', 5),
    ('Зина', 3),
    ('Гермиона', 4),
    ('Гермиона', 4),
    ('александр', 4),
]
print_order_rating(drivers)

print()

drivers = [
    ('Джек', 2),
    ('Джек', 3),
    ('Гермиона', 5),
    ('Билл', 4),
    ('Билл', 4),
    ('Гермиона', 3),
    ('Джек', 2),
    ('ЯЯ', 5),
    ('ФФФ', 5),
    ('Билл', 4),
    ('Укк', 4),
    ('Билл', 3),
    ('Джек', 2),
    ('Джек', 2),
    ('Гермиона', 5),
    ('Билл', 2),
    ('ФФФ', 4),
    ('Билл', 3),
    ('ФФФ', 3),
    ('Джек', 2),
    ('Джек', 1),
    ('Гермиона', 5),
    ('Билл', 2),
    ('Курт', 5),
    ('Билл', 3),
]
print_order_rating(drivers)