def sum_recursive(numbers):
    total = 0
    for item in numbers:
        if isinstance(item, list):
            total += sum_recursive(item)
        else:
            total += item
    return total

print(sum_recursive([1, 2, 3, 4, 5]))
print(sum_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
print(sum_recursive([1, 2, 3, 4, [[5]], [5]]))