def increase_3(num_list):
    return tuple(map(lambda x: x * 3, num_list))

numbers = [16, -1, 8, 6, -5, -9, 22, 26, 7, -10]
print(increase_3(numbers))

