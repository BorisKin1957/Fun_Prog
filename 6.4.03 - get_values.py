def get_values(nums: tuple[int, ...]) -> tuple[int, ...]:
    result = filter(lambda x: x % 3 == 0, nums)
    return tuple(map(lambda x: x * 3, result))

nums = (2, 12, 5, 9, 3, 16, 7, 13, 21, 1, 15, 4, 20, 11)
print(get_values(nums))

nums = (2, 0, 3, 4, 7, 13, 21, 1, 15, 9, 11)
print(get_values(nums))