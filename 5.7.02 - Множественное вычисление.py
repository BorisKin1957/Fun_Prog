def compute(list_of_function, *args):
    return [func(arg) for func in list_of_function for arg in args]

def square(num):
    return num ** 2

def inc(num):
    return num + 1

def dec(num):
    return num - 1

print(compute([square, inc, dec], 10))

print()

def square(num):
    return num ** 2

def inc(num):
    return num + 1

def dec(num):
    return num - 1

print(compute([inc, dec, square], 10, 20, 30, 40))

print()

def inc(num):
    return num + 1

def dec(num):
    return num - 1

def repeater(value, n=10):
    return str(value) * n

def square(num):
    return num ** 2

print(compute([repeater, dec, inc, square], 5, 7, 0, True))