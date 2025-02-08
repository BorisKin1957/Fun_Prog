def fibonacci(n):
    if n <= 1:
        yield n
    return fibonacci(n - 1) + fibonacci(n - 2)



for i in fibonacci(5):
    print(i)