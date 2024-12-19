def countdown(limit):
    count = limit
    def inner():
        nonlocal count
        if count > 0:
            print(count)
        else:
            print(f'Превышен лимит, вы вызвали более {limit} раз')
        count -= 1
    return inner


count = countdown(3)
count()
count()
count()
count()
count()

print()

a = countdown(2)
b = countdown(2)
a()
b()
b()
b()
a()
a()