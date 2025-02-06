def find_level_element(value, lst, level=1):
    for item in lst:
        if item == value:
            return level
        elif isinstance(item, list):
            result = find_level_element(value, item, level + 1)
            if result != -1:
                return result
    return -1


print(find_level_element(1, [1, 2, 3, 4, 5, [5]]))
print(find_level_element(5, [1, 2, 3, 4, [[5]], [5]]))
print(find_level_element(9, [1, 2, 3, 4, 5,
                             [6, 7, 8,
                              [[[9]], 1, [2, [3], 4], 5, 6]]]))