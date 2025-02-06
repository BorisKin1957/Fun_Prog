def validate_all_kwargs_int_pos(func):
    def wrapper(*args, **kwargs):
        flag = True
        for arg in kwargs.values():
            if not (isinstance(arg, int) and arg > 0):
                flag = False
                break
        if flag:
            return func(*args, **kwargs)
        else:
            print("Все именованные аргументы должны быть положительными числами")
    return wrapper

def validate_all_args_str(func):
    def wrapper(*args, **kwargs):
        flag = True
        for arg in args:
            if not isinstance(arg, str):
                flag = False
                break
        if flag:
            return func(*args, **kwargs)
        else:
            print("Все аргументы должны быть строками")
    return wrapper

@validate_all_kwargs_int_pos
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate(a="i", b='Love', c="Python"))

print()

@validate_all_kwargs_int_pos
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate(a=10, b=20, c=50))

print()

@validate_all_args_str
@validate_all_kwargs_int_pos
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result

print(concatenate('Hello', 2, 'World', a="i", b='Love', c="Python"))