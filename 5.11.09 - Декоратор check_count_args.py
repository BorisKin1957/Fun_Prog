from functools import wraps

def check_count_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        lenght = len(args) + len(kwargs)
        if lenght < 2:
            print('Not enough arguments')
        elif lenght > 2:
            print('Too many arguments')
        else:
            return func(*args, **kwargs)
    return wrapper


@check_count_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y


print(add_numbers(4, 5))
print(add_numbers.__name__)
print(add_numbers.__doc__.strip())

print()

@check_count_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y

add_numbers(4)