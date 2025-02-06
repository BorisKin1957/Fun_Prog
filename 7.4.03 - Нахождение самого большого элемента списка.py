
def get_max_recursive(lst, L=None):
    if L is None:
        L = []
    for i in lst:
        if isinstance(i, int):
            L.append(i)
        else:
            get_max_recursive(i, L)
    return max(L)



print(get_max_recursive([1, 2, 3, 4, 9]))
print(get_max_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
print(get_max_recursive([1, 2, 3, 4, [[5]], [5]]))

