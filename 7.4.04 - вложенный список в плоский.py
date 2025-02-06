def flatten(lst, L=None):
    if L is None:
        L = []
    for i in lst:
        if isinstance(i, int):
            L.append(i)
        else:
            flatten(i, L)
    return L

print(flatten([1, 2, 3, 4, 9]))
print(flatten([[1, 2, 3], [4, 5], [6, 7, 8]]))
print(flatten([1, 2, 3, 4, [[5]], [5]]))
print(flatten([[[[[[[[[4]]]]]], [[[[[[[5, 6, 7, [5, [4]]]]]]]]]]]]))