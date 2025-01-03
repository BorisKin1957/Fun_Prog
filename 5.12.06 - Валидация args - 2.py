from functools import wraps


def validate_all_args(type_):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            flag = True
            for arg in args:
                if not isinstance(arg, type_):
                    flag = False
                    break
            if flag:
                return func(*args, **kwargs)
            else:
                print(f'Все аргументы должны принадлежать типу {type_}')
        return wrapper
    return decorator


@validate_all_args(str)
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)

print()

@validate_all_args(int)
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)