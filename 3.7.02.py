def concatenate(**kwargs):
    result = ''
    for i in kwargs.values():
        result += str(i)
    return result

print(concatenate(t='Happy', y="Meal", w="Cost", m=10, b='Buks'))