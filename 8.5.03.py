def flatten(lst):
    for value in lst:
        if isinstance(value, list):
            yield from flatten(value)
        else:
            yield value


gen = flatten([[[1, [5]]], [2], [4, 5, [6]]])
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))