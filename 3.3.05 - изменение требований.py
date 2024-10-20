def is_table_free(number: int) -> bool:
    return not tables[number]

def reserve_table(number: int, name: str, status:  bool) -> dict:
    if is_table_free(number):
        tables[number] = {'name': name, 'is_vip': status}

    return tables

def delete_reservation(number):
    tables[number] = None
    return tables

tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: None,
}

print(tables)
reserve_table(3, 'Gena', True)
reserve_table(4, 'Artem', False)
reserve_table(5, 'Artur', True)  # Артур не должен занять место Василия
print(tables)

print()

tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: None,
}
print(tables)
delete_reservation(5)
delete_reservation(4)
reserve_table(9, 'Igor', False)
reserve_table(8, 'Nika', False)
reserve_table(7, 'Zhanna', False)
print(tables)