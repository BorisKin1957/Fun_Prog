'''Функция filter_list принимает на вход функцию f и список l.
Возвращает список, состоящий из элементов списка l,
для которых функция f возвращает True.'''


def filter_list(f: callable, l: list)-> list:
    return [i for i in l if f(i)]

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_list(is_even, numbers) # берем только четные
print(even_numbers)

print()

def is_positive(num):
    return num > 0

numbers = [-1, 2, -3, 4, 5, -6, 7, -8, -9, 10]
positive_numbers = filter_list(is_positive, numbers) # берем только положительные
print(positive_numbers)