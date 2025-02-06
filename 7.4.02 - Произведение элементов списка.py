def multu_recursive(numbers):
    total = 1
    for item in numbers:
        if isinstance(item, list):
            total *= multu_recursive(item)
        elif isinstance(item, int):
            total *= item
    return total


print(multu_recursive([1, 2, 3, 4, 5]))
print(multu_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
print(multu_recursive([1, 2, 3, 4, [[5]], [5]]))

print(multu_recursive(['1', '2', '3', '4', '5']))