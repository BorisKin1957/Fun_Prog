def my_enumerate(lst: list[str], start: int = 0) -> list[tuple[int, str]]:
    '''копирует работу встроенной функции enumerate'''
    for word in lst:
        yield (start, word)
        start += 1
        
lessons = ["Что такое функция", "Возвращаемое значение",
           "Параметры и аргументы функции",
           "Чистая функция", "Параметр *args"]

for i, lesson in my_enumerate(lessons):
    print("Урок {}: {}".format(i, lesson))

lessons = ["Что такое функция", "Возвращаемое значение",
           "Параметры и аргументы функции",
           "Чистая функция", "Параметр *args", "Параметр **kwargs"]

for i, lesson in my_enumerate(lessons, 1):
    print("Урок {}: {}".format(i, lesson))