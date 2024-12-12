def aggregation(func, secuence, initial=None):
    if initial is None:
        result = secuence[0]
        lst = secuence[1:]
    else:
        result = initial
        lst = secuence
    for num in lst:
        result = func(result, num)
    return result


def get_add(x, y):
    return x + y


print(aggregation(get_add, [5, 2, 4, 3, 5], initial=10))

print()

def get_add(x, y):
    return x + y

print(aggregation(get_add, [11, 4, 5, 7, 8, 10]))

print()

print(aggregation(lambda x, y: x + y, [4, 5, 6], initial=100))

print()

def get_product(x, y):
    return x * y

print(aggregation(get_product, [2, 5, 10, 1, 2]))