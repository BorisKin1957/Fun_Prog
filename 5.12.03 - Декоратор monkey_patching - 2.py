from functools import wraps


def monkey_patching(arg='Monkey', kwarg='patching'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args = (arg for _ in args)
            kwargs = {key: kwarg for key, value in kwargs.items()}
            return func(*args, **kwargs)
        return wrapper
    return decorator


@monkey_patching(arg='Super')
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)

print()


@monkey_patching(kwarg='Duper')
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)