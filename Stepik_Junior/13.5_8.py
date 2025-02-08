'''
Правильная скобочная последовательность 🌶️

Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text,
состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является
правильной скобочной последовательностью и False в противном случае.

Примечание 1. Правильной скобочной последовательностью называется строка,
состоящая только из символов ( и ), где каждой открывающей скобке найдется парная закрывающая скобка.

Примечание 2. Следующий программный код:

print(is_correct_bracket('()(()())'))
print(is_correct_bracket(')(())('))

должен выводить:

True
False

Sample Input:
((()))

Sample Output:
True

'''


# объявление функции
def is_correct_bracket(s):
    c, c1 = 0, 0

    for i in range(len(s)):
        if s[i] == '(':
            c += 1
        else:
            c1 += 1
        if c1 > c:
            result = False
            break
        else:
            result = True
        if c != c1:
            result = False
    return result


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
