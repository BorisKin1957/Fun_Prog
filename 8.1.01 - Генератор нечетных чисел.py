def gen_odd(n):
    for i in range(1, n + 1, 2):
        yield i


print(*gen_odd(10))

for value in gen_odd(5):
    print(value)

gen = gen_odd(6)
print(next(gen))
print(next(gen))
print(next(gen))
try:
    next(gen)
except StopIteration:
    print('Завершили обход генератора')
else:
    raise ValueError('Вы создали не генератор')