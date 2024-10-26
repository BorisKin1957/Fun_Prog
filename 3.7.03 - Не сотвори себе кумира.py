def create_actor(**kwargs):
    basis_dict = {'name': 'Райан', 'surname': 'Рейнольдс', 'age': 47}
    # if not kwargs:
    #     return basis_dict
    return {**basis_dict, **kwargs}


actor = create_actor()
print(actor)


actor = create_actor(
    height=190,
    movies=['Дедпул', 'Главный герой']
)
print(actor)

actor = create_actor(
    name='Jack',
    age=20,
    surname='Qwerty')
print(actor)

actor = create_actor(surname='Уиллис', age=69, name='Брюс')
print(actor)