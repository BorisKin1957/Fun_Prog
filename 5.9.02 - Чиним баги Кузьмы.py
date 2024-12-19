def decorator(func):
    def wrapper(x, y):
        print('---Start calculation---')
        result = func(x, y)
        print(f'---Finish calculation. Result is {result}---')
        return result
    return wrapper


@decorator
def add(a, b):
    return a + b

add(1, 4)

print()

add(10, 20)
add(50, 7)