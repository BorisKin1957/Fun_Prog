def reserve_table(number: int, name: str, status: bool = False) -> dict:
    if tables.get(number) is None:
        tables[number] = {'name': name, 'is_vip': status, 'order': {}}  # Создаем таблицу
    return tables[number]


def make_order(number: int, **kwargs: dict) -> dict:
    D, new, product = {}, {}, ['salad','soup', 'main_dish', 'drink', 'desert']
    for key in kwargs:
        if key in product:
            new.setdefault(key, kwargs[key])
    D.setdefault('order', new)
    return reserve_table(number, tables[number]['name'])['order'].update(D['order'])


def delete_order(*, number_table: int, delete_all: bool = False, **kwargs) -> None:
    if delete_all:
        tables[number_table]['order'] = {}
    else:
        for key in kwargs:
            if kwargs[key]:
                tables[number_table]['order'].pop(key, None)


tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

make_order(1, soup='Borsh')
make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')

reserve_table(2, 'Vlad')

make_order(2, soup='Чечевичный', salad='Цезарь', breakfast='Яичница')
make_order(2, drink='Raf', main_dish='Утка по-пекински')
make_order(2, desert='Трюфель', call='такси')
print(tables)

delete_order(number_table=2, delete_all=True)
print(tables)

print('----------------------------')
tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Borsh'}},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

try:
    delete_order(1, delete_all=True)
except TypeError:
    print('Вызов delete_order без передачи значения по ключу не должен проходить')
else:
    raise ValueError('Проверьте типы параметров функции delete_order')

print('----------------------------')

tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Borsh'}},
    2: None,
    3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

make_order(1, soup='Borsh')
make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')

reserve_table(2, 'Vlad')

make_order(2, soup='Чечевичный', salad='Цезарь', breakfast='Яичница')
make_order(2, drink='Raf', main_dish='Утка по-пекински')
make_order(2, desert='Трюфель', call='такси')
print(tables)

delete_order(number_table=2, salad=True, main_dish=True, soup=False, desert=True)
print(tables)