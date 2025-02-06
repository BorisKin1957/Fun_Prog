def reversed_recursive(lst):
    if isinstance(lst, list):
        return [reversed_recursive(item) for item in lst[::-1]]
    return lst




print(reversed_recursive([1,2,3]))
print()
print(reversed_recursive([[1, 2, 3], [4, [5, [6]]], 7]))