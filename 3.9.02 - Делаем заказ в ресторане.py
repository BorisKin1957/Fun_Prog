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