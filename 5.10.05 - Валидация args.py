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

@validate_all_args_str
def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += str(arg)
    return result


print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))

print()

@validate_all_args_str
def concatenate(*args):
    result = ""
    for arg in args:
        result += arg
    return result


print(concatenate("Через", 9, "Месяцев"))

print()

@validate_all_args_str
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result

print(concatenate("Я", "думаю", "Выучить", "Питон", a="За", b=10, c="Месяцев"))

print()

@validate_all_args_str
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate('Hello', 9, 'World', a=10, b=20, c=30))