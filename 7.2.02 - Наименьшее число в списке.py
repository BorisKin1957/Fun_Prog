def find_min(numbers: list) -> int:
    if len(numbers) == 1:
        return numbers[0]
    else:
        if numbers[0] < numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0]
        return find_min(numbers[1:])

numbers = [10, 32, 24, 17, -5, 10, -22]
print(find_min(numbers))

numbers = [-230, 101, 323, -200, 17, -5, 10, -22]
print(find_min(numbers))