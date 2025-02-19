def lstrip(lst, item):
    result = lst[::]
    while result and result[0] == item:
        result.pop(0)
    return result

data = [0, 0, 0, 1, 0, 2, 3, 0, 0]
print(data)
print(lstrip(data, 0))
print(data)