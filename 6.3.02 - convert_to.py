def convert_to(values, type_to=int):
    #return [type_to(value) for value in values]
    return list(map(type_to, values))


numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150]
print(convert_to(numbers, str))
