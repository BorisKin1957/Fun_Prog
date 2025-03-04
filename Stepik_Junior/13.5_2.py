'''Is a Number Prime? 🌶️

Напишите функцию is_prime(num), которая принимает в качестве аргумента
натуральное число и возвращает значение True если число является простым и False в противном случае.

 Примечание. Следующий программный код:

print(is_prime(1))
print(is_prime(10))
print(is_prime(17))

должен выводить:

False
False
True
'''


# объявление функции
def is_prime(num):
    a = True
    if num == 1:
        a = False
    for i in range(2, num):
        if num % i == 0:
            a = False
            break
    return a


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
