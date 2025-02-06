def zip_with_function(numbers, function):
    result = [function(*i) for i in zip(*numbers)]
    return result

def get_sum_two_numbers(a: int, b: int) -> int:
    return a + b


print(zip_with_function([[1, 2, 4], [3, 5, 8]], get_sum_two_numbers))

def get_sum_two_numbers(a: int, b: int) -> int:
    return a + b

print(zip_with_function([[10, 20], [30, 0]], get_sum_two_numbers))