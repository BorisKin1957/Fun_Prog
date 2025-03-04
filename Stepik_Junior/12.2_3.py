"""Сумма чисел

На вход программе подается строка текста, содержащая натуральные числа.
Напишите программу, которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Строковый метод join() работает только со списком строк.
Тестовые данные 🟢

Sample Input 1:
2 5 11 33 55

Sample Output 1:
2+5+11+33+55=106

"""

sum = 0
s = []

for num in input().split():
    sum += int(num)
    s.append(num)
    
s = '+'.join(s)
s += '='

print(s, sum, sep='')
