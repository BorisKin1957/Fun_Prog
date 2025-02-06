from functools import wraps

def cache_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in wrapper.cache:
            result = wrapper.cache[args]
            print(f'[FROM CACHE] Вызов {func.__name__} = {result}')
            return result
        elif kwargs:
            key = tuple(kwargs.items())
            if key in wrapper.cache:
                result = wrapper.cache[key]
                print(f'[FROM CACHE] Вызов {func.__name__} = {result}')
                return result
            else:
                result = func(*args, **kwargs)
                wrapper.cache[key] = result
                return result
        else:
            result = func(*args, **kwargs)
            wrapper.cache[args] = result
            return result

    wrapper.cache = {}
    return wrapper

@cache_result
def multiply(a, b):
    return a * b


print(multiply(4, 5))
print(multiply(4, 5))
print(multiply(4, 5))
print(multiply(5, 4))
print(multiply.__name__)

print()

@cache_result
def add(a, b):
    return a + b

print(add(4, 4)) # 1й раз с такими атрибутами
print(add(4, 5)) # 1й раз с такими атрибутами
print(add(4, 6)) # 1й раз с такими атрибутами
print(add(4, 5)) # достаем из кеша
print(add(5, 4)) # 1й раз с такими атрибутами
print(add(6, 3)) # 1й раз с такими атрибутами
print(add(a=6, b=3)) # 1й раз с такими атрибутами: позицицинные!=именованные
print(add(a=6, b=3)) # достаем из кеша