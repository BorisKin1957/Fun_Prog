'''Искомый месяц

Напишите функцию get_month(language, number), которая принимает на вход два аргумента
language – язык ru или en и number – номер месяца (от 1 до 12) и
возвращает название месяца на русском или английском языке.

Примечание. Следующий программный код:

print(get_month('ru', 1))
print(get_month('ru', 12))
print(get_month('en', 1))
print(get_month('en', 10))

должен выводить:

январь
декабрь
january
october

'''


# объявление функции
def get_month(lang, numb):
    ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
          'декабрь']
    en = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
          'november', 'december']
    if lang == 'ru':
        return ru[num]
    else:
        return en[num]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
