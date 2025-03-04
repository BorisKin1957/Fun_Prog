'''Тимур и его числа

Тимур загадал число от 1 до n.
За какое наименьшее количество вопросов
(на которые Тимур отвечает "больше" или "меньше")
Руслан может гарантированно угадать число Тимура?

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести наименьшее количество вопросов,
которых гарантированно хватит Руслану, чтобы угадать число Тимура.
Тестовые данные 🟢

Sample Input 1:
8

Sample Output 1:
3
'''

n, count = int(input()), 0
while n > 1:
  n = n / 2
  count += 1

print(count)