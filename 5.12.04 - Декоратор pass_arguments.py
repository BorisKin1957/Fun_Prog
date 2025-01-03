from functools import wraps

def pass_arguments(*args1, **kwargs1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            return func(*(args1 + args), **(kwargs | kwargs1))
        return wrapper
    return decorator


@pass_arguments(1, 2, 3)
def add(*values):
    return sum(values)


print(add(5, 4, 6))

print()

@pass_arguments(s='Когда', w='-', r='нибудь!')
def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += str(arg)
    return result


print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))