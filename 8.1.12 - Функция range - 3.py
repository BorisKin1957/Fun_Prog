def my_range_gen(*args):
    if len(args) == 1:
        i = 0
        while i < args[0]:
            yield i
            i += 1
    elif len(args) == 2:
        i, end = args[0], args[1]
        while i < end:
            yield i
            i += 1
    else:
        if args[2] > 0:
            i, end, step = args[0], args[1], args[2]
            while i < end:
                yield i
                i += step
        if args[2] < 0:
            i, end, step = args[0], args[1], args[2]
            while i > end:
                yield i
                i += step




for i in my_range_gen(30, 1, -5):
    print(i)
print()

for i in my_range_gen(4, 8, 0):
    print(i)


print()

for i in my_range_gen(5):
    print(i)

for i in my_range_gen(10, 30, 3):
    print(i)

for i in my_range_gen(10, 20):
    print(i)
print('**********************')

for i in my_range_gen(1, 10, -2):
    print(i)

for i in my_range_gen(4, 8, 0):
    print(i) # Ничего не печатает
for i in my_range_gen(20, 10, 3):
    print(i)
print('End')

for i in my_range_gen(25, 0, -5):
    print(i)
