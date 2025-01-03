from functools import wraps

def convert_to(new_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return new_type(func(*args, **kwargs))
        return wrapper
    return decorator


@convert_to(int)
def add_values(a, b):
    return a + b


result = add_values(10, 20)
print(f"Результат: {result}, тип результата {type(result)}")

print()

@convert_to(str)
def add_values(a, b):
    return a + b


result = add_values(10, 20)
print(f"Результат: {result}, тип результата {type(result)}")

print()

@convert_to(list)
def add_values(a, b):
    return a + b


result = add_values('hello', 'world')
print(f"Результат: {result}, тип результата {type(result)}")
