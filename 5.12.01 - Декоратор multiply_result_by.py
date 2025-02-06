from functools import wraps

def multiply_result_by(number):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * number
        return wrapper
    return decorator


@multiply_result_by(2)
def my_function(x, y):
    return x + y


print(my_function(5, 6))

print()

@multiply_result_by(3)
@multiply_result_by(4)
def my_function(x, y):
    return x + y


print(my_function(2, 3))