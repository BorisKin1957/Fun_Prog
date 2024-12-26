from functools import wraps

def add_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new = ('begin',) + args + ('end',)
        return func(*new, **kwargs)
    return wrapper


@add_args
def concatenate(*args):
    """
    Возвращает конкатенацию переданных строк
    """
    return ', '.join(args)


print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
print(concatenate('my', 'name is', 'Artem'))
print(concatenate.__name__)
print(concatenate.__doc__.strip())