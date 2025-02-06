def uppercase_elements(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, dict):
            result = {}
            for key, value in res.items():
                if isinstance(key, str):
                    result[key.upper()] = value
                else:
                    result[key] = value
            return result
        else:
            result = []
            for element in res:
                if isinstance(element, str):
                    result.append(element.upper())
                else:
                    result.append(element)
            return result
    return wrapper


@uppercase_elements
def my_func():
    return ['monarch', 'Touch', 'officiaL', 'DangerouS', 'breathe']

print(my_func())

print()

@uppercase_elements
def my_func(name, surname):
    return ['temple', 'store', name, surname, *[1, 2, 3]]

print(my_func('Gerard', 'Pique'))

print()

@uppercase_elements
def my_func(**kwargs):
    return {1: 'one', 2: 'store', 'three': 3, 'four': 4} | kwargs

print(my_func(**{'Five': 5, 'sIx': 6}))