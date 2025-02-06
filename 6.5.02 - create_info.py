def create_info(employees: list, identifiers: list) -> dict:
    '''create_info на основании параметров employees и identifiers должна создать словарь,
    ключами которого являются идентификаторы, а значениями - имена сотрудников.'''
    return dict(zip(sorted(identifiers), sorted(employees)))


names = [
    'Pankratiy', 'Lidochka', 'Svetka', 'Maks', 'Yura', 'Sergei'
]

ids = [77, 4, 20, 37, 32, 96]
print(create_info(names, ids))

names = [
    'Pankratiy', 'Lidochka', 'Innokentiy', 'Anfisa', 'Yaroslava',
    'Svetka', 'Maks', 'Yura', 'Sergei'
]

ids = [77, 4, 20, 5, 56, 17, 20, 32, 96]
print(create_info(names, ids))

