def is_member(value, lst):
    for item in lst:
        if isinstance(item, list):
            if is_member(value, item):
                return True
        elif item == value:
            return True
    return False

print(is_member(9, [[1, 2, 3], [4, 5], [6, 7, 8]]))
print(is_member(9, [1, 2, 3, 4, 5,
                 [6, 7, 8,
                  [9, 1, [2, [3], 4], 5, 6]]]))