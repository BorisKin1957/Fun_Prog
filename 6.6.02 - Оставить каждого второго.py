def even_items(iterable):
    return [value for key, value in enumerate(iterable, 1) if key % 2 == 0]


print(even_items([3, 7, 5, 6, 3, 8, 9]))
