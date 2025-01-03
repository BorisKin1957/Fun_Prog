from functools import wraps

def compose(*funcs):
    def decoder(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for f in funcs:
                result = f(result)
            return result
        return wrapper
    return decoder


def double_it(a):
    return a * 2


def increment(a):
    return a + 1


@compose(double_it, increment)
def get_sum(*args):
    return sum(args)


print(get_sum(5))
print(get_sum(20, 10))
print(get_sum(5, 15, 25))