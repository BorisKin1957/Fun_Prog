from functools import wraps


def add_attrs(**kw):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for key, value in kw.items():
                setattr(wrapper, key, value)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@add_attrs(test=True, ordered=True)
def add(a, b):
    return a + b

print(add(10, 5))
print(add.test)
print(add.ordered)