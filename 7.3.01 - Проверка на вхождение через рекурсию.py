def is_member(value, lst):
    if not lst:
        return False
    if lst[0] == value:
        return True
    return is_member(value, lst[1:])


print(is_member("e", ['a', 'e', 'i', 'o', 'u']))
print(is_member(10, [1, 23, 3, 43, 10, 35]))
print(is_member(10, [1, 2, 3, 4, 5]))
print(is_member(10, []))
print(is_member(10, [10]))
