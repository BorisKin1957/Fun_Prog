from functools import wraps

def no_side_effects_decorator(func):
    @wraps(func)
    def wrapper(*args):
        return func(*(args[0].copy(), *args[1:]))
    return wrapper


@no_side_effects_decorator
def add_element(data, element):
    data.append(element)
    return data


my_list = [1, 2, 3]
print('Результат вызова =', add_element(my_list, 4))
print('Результат вызова =', add_element(my_list, 5))
print(my_list)
print(add_element.__name__)

print()

@no_side_effects_decorator
def add_element(data, key, value=None):
    data[key] = value
    return data


my_dict = {1: 'Hello', 2: 'World'}
print('Результат вызова =', add_element(my_dict, 3))
print('Результат вызова =', add_element(my_dict, 4, 'four'))
print(my_dict)
print(add_element.__name__)