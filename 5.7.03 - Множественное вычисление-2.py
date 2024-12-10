def compute(list_of_functions, *args):
    result = []
    for arg in args:
        new = list_of_functions[0](arg)
        for func in list_of_functions[1:]:
            new = func(new)
        result.append(new)
    return result


def square(num):
    return num ** 2

def inc(num):
    return num + 1

def dec(num):
    return num - 1

print(compute([square, inc], 10))

print()

def square(num):
    return num ** 2

def inc(num):
    return num + 1

def dec(num):
    return num - 1

print(compute([inc, square, dec], 10, 20, 30, 40))

print()

def inc(num):
    return num + 1

def dec(num):
    return num - 1

def repeater(value, n=3):
    return str(value) * n

def square(num):
    return num ** 2

print(compute([dec, inc, square, repeater], 5, 7, 0, True))