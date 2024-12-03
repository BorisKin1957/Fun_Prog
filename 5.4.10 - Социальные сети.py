def print_statistic(list_posts):
    new, result = {}, {}
    for post in list_posts:
        new.setdefault(post[0],set()).add(post[1])
    result = sorted(new.items(), key=lambda x: (-len(x[1]), x[0].lower()))
    for item in result:
        print(f'Количество уникальных комментаторов у {item[0]} - {len(item[1])}')



data = [
    ('karl', 'makron78'),
    ('karl', 'realdonaldtrump'),
    ('qwery07', 'makron78'),
    ('Billy', 'realdonaldtrump'),
    ('Billy', 'realdonaldtrump'),
    ('qwery07', 'joebiden'),
    ('karl', 'joebiden'),
]
print_statistic(data)

print()

data = [
    ('karl', 'zhanna777'),
    ('karl', 'мама_игоречка_98'),
    ('qwerty03', 'pushka76'),
    ('Billy', 'мама_игоречка_98'),
    ('Billy', 'pushka76'),
    ('qwerty03', 'joebiden'),
    ('karl', 'zhanna777'),
    ('karl', 'joebiden'),
    ('karl', 'pushka76'),
]

print_statistic(data)

print()

data = [
    ('7', 'opushka'),
    ('1', 'opushka'),
    ('2', 'opushka'),
    ('3', 'opushka'),
    ('2', 'opushka'),
    ('1', 'opushka'),
    ('2', 'opushka'),
    ('5', 'opushka'),
    ('6', 'opushka'),
    ('6', 'opushka'),
]

print_statistic(data)