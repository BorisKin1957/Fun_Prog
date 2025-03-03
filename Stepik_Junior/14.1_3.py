'''Биномиальный коэффициент 🌶️

Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов
два натуральных числа n и k и возвращает значение биномиального коэффициента, равного n! / ((k! * (n−k)!).

Примечание 1. Факториалом натурального числа nn, называется произведение всех натуральных чисел от 1 до n, то есть
n!=1⋅2⋅3⋅…⋅n
n!=1⋅2⋅3⋅…⋅n

Примечание 2. Реализуйте вспомогательную функцию factorial(n),
вычисляющую факториал числа или воспользуйтесь уже готовой функцией из модуля math.
'''


# объявление функции
def compute_binom(n, k):
    from math import factorial

    return int(factorial(n) / (factorial(k) * factorial(n - k)))


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
