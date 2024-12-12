def aggregation(func, secuence):
    result = [func(secuence[0], secuence[1])]
    for i in range(len(secuence[1:]) - 1):
        result.append(func(result[i], secuence[i + 2]))
    return result

def get_add(x, y):
    return x + y

print(aggregation(get_add, [5, 2, 4, 3, 5]))

print()

def get_max(x, y):
    return max(x, y)

# агрегируем нахождение максимума
print(aggregation(get_max, [1, 4, 5, 7, 6, 5, 8, 10]))

print()

def get_min(x, y):
    return min(x, y)

# агрегируем нахождение минимума
print(aggregation(get_min, [9, 6, 7, 8, 5, 1, 2, 4]))

print()

def get_product(x, y):
    return x * y

print(aggregation(get_product, [2, 6, 5, 10, 5, 1, 2]))