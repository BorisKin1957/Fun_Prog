def filter_even(func):
    def wrapper(*args, **kwargs):
        result = []
        for arg in args:
            if isinstance(arg, (list, set, dict, tuple, str)):
                if len(arg) % 2 == 0:
                    result.append(arg)
            elif isinstance(arg, (int, float)):
                if arg % 2 == 0:
                    result.append(arg)
            elif isinstance(arg, bool):
                result.append(arg)
        #print(tuple(result))
        return func(*result, **kwargs)
    return wrapper

def delete_short(func):
    def wrapper(*args, **kwargs):
        result = dict(filter(lambda x: len(str(x[0])) > 4, kwargs.items()))
        #new = dict(result)
        #print(new)
        return func(*args, **result)
    return wrapper

@delete_short
def info_kwargs(**kwargs):
    """Выводит информацию о переданных kwargs"""
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')

info_kwargs(first_name="John", last_name="Doe", age=33)

print()

@filter_even
def concatenate(*args):
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))

print()

@filter_even
@delete_short
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate("Я", "хочу", "Выучить", "Питон", a="За", qwerty=10, c="Месяцев"))