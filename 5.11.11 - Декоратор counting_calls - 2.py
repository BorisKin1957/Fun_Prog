from functools import wraps

def counting_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        wrapper.calls.append({'args': args, 'kwargs': kwargs})
        return func(*args, **kwargs)
    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper


@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b


print(add.__name__)
print(add.__doc__)

print(add(10, b=20))
print('Количество вызовов =', add.call_count)
print(add.calls)

print(add(5, 6))
print(add.calls[1])

print()

@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, b=20))
print(add(7, 5))
print(add(12, 45))
print('Количество вызовов =', add.call_count)
print(add.calls[2])

print(add(b=11, a=22))
print(add.calls[3])