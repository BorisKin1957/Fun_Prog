def flatten_matrix(lst):
    for value in lst:
        if isinstance(value, list):
            yield from flatten_matrix(value)
        else:
            yield value


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(flatten_matrix(nested_list)))

nested_list = [[1, 7], [6, 5], [3, 2], [9, 2]]
gen = flatten_matrix(nested_list)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))