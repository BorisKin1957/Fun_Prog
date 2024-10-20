def is_table_free(number: int) -> bool:
    return not tables[number]

def reserve_table(number: int, name: str) -> dict:
    if is_table_free(number):
        tables[number] = name
    return tables

def delete_reservation(number):
    tables[number] = None
    return tables

tables = {
    1: 'Andrey',
    2: None,
    3: 'Gena',
    4: 'Artem',
    5: 'Vasiliy',
    6: None,
    7: 'Artur',
    8: None,
    9: 'Misha',
}
print(tables)
delete_reservation(1)
delete_reservation(3)
reserve_table(6, 'Chubaka')
print(tables)
