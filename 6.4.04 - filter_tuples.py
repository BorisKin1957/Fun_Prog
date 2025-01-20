def filter_tuples(nums: tuple[tuple[int]]) -> tuple[tuple[int, ...]]:
    return tuple(filter(lambda x: x[0] * x[1] * x[2] == 60 and len(x) == 3, nums))


numbers = (
    (1, 2, 3), (1, 2, 30, 4),
    (1, 20, 3), (15, 2, 3),
    (10, 2, 3), (10, 20, 30),
)
print(filter_tuples(numbers))

numbers = (
    (1, 2, 3), (1, 2, 30),
    (1, 20, 3), (5, 3, 4),
    (5, 12, 1), (5, 12, 0),
    (5, 5, 12), (15, 2, 3),
    (10, 2, 3), (10, 20, 30),
    (1, 2, 30), (60, 1, 1),
    (60, 1, 0), (20, 2, 2),
)
print(filter_tuples(numbers))