def apply(func, args):
    result = [func(arg) for arg in args]
    return result


def square(num):
    return num ** 2

print(apply(square, [5, 7, 0, 3]))

print()


def repeater(value, n=5):
    return str(value) * n

print(apply(repeater, ['Hi', True, 0, [1, 2]]))

print()

def repeater(value, n=5):
    return str(value) * n


print(apply(repeater, 'hello'))