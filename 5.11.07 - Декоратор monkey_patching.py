from functools import wraps

def monkey_patching(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = ('Monkey' for arg in args)
        kwargs = {key: 'patching' for key, value in kwargs.items()}
        return func(*args, **kwargs)
    return wrapper

@monkey_patching
def concatenate(*args):
    """
    Возвращает конкатенацию переданных строк
    """
    return ', '.join(args)


print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
print(concatenate('my', 'name is', 'Artem'))
print(concatenate.__name__)
print(concatenate.__doc__.strip())

print()

@monkey_patching
def info_kwargs(**kwargs):
    """Выводит информацию о переданных kwargs"""
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')

info_kwargs(first_name="John", last_name="Doe", age=33)
info_kwargs(c=43, b= 32, a=32)
print(info_kwargs.__name__)
print(info_kwargs.__doc__.strip())