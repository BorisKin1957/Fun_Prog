def reserve_table(number: int, name: str, status: bool = False) -> dict:
    if tables.get(number) is None:
        tables[number] = {'name': name, 'is_vip': status, 'order': {}}  # Создаем таблицу
    return tables[number]


def make_order(number: int, new={}, **kwargs: dict) -> dict:
    D, product = {}, ['salad', 'soup', 'main_dish', 'drink', 'desert']
    for key, value in kwargs.items():
        if key in product:
            new[key] = new.get(key, []) + value.split(',')

    D.setdefault('order', new)
    return reserve_table(number, tables[number]['name'])['order'].update(D['order'])

def delete_order(*, number_table: int, delete_all: bool = False, **kwargs) -> None:
    if delete_all:
        tables[number_table]['order'] = {}
    else:
        for key in kwargs:
            if kwargs[key]:
                tables[number_table]['order'].pop(key, None)


# tables = {
#     1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
#     2: None,
#     3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
# }
# make_order(1, soup='Borsh')
# make_order(1, soup='Лапша')
# print(tables)

print('-' * 20)

# tables = {
#     1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
#     2: None,
#     3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
# }
# make_order(1, soup='Borsh,Лапша', desert='Медовик', drink='Cola')
# make_order(1, soup='Гаспачо', desert='Печенье,Наполеон')
# print(tables)

print('-' * 20)

tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

make_order(1, soup='Borsh,Лапша', desert='Медовик', drink='Cola')
make_order(1, soup='Гаспачо', desert='Печенье,Наполеон')

reserve_table(2, 'Vlad')

make_order(2, soup='Чечевичный', salad='Цезарь,Мимоза', breakfast='Яичница,Бекон')
make_order(2, drink='Raf,Coffee,Juice', main_dish='Утка по-пекински,Отбивная')
make_order(2, desert='Трюфель', call='такси')

make_order(1, desert='Наполеон', drink='Чай', meal='Манка,Овсянка')
make_order(1, desert='Вишня', drink='Кофе')
print(tables)
delete_order(number_table=2, drink=True, desert=True, call=True, шаурма=True, cheesecake=True)
delete_order(number_table=1, soup=True, desert=True, call=True)
print(tables)