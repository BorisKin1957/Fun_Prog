def repeater(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            func(*args, **kwargs)
    return wrapper


@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(9, 4)

print()


@repeater
def some_func(a, b, c):
    print(a ** b + c)


some_func(4, 5, 4)
some_func(14, 51, 34)