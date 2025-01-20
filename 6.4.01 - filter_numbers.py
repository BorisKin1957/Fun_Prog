def filter_numbers(numbers):
    #return [number for number in numbers if (number % 2 == 0 or abs(number) > 100)]
    return list(filter(lambda x: x % 2 == 0 or abs(x) > 100, numbers))


numbers = [1, 2, 3, 4, 5, 6, 7]
print(filter_numbers(numbers))

numbers = [-100, 2, -300, -400, 5, -60, -61, -101, 101]
print(filter_numbers(numbers))