'''Звездный треугольник 🌶️

Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник
с основанием и высотой равными 15 и 8 соответственно:

       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************

Примечание 1 . Для вывода треугольника используйте цикл for.

Примечание 2 . Справа от звездочек пробелов нет.

'''


# объявление функции
def draw_triangle(line, col):
    for i in range(line):
        print(' ' * (line - 1 - i) + '*' * (1 + i * 2))


# основная программа
draw_triangle(8, 15)  # вызов функции