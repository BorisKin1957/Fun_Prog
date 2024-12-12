def aggregation(func, secuence):
    result = secuence[0]
    for num in secuence[1:]:
        result = func(result, num)
    return result


def get_add(x, y):
    return x + y

print(aggregation(get_add, [5, 2, 4, 3, 5]))

print()

def get_min(x, y):
    return min(x, y)

# агрегируем нахождение минимума
print(aggregation(get_min, [9, 6, 7, 8, 5, 1, 2, 4]))