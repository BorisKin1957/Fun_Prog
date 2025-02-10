def my_range_gen(*args):
    if len(args) == 1:
        for i in range(args[0]):
            yield i
    else:
        for i in range(args[0], args[1]):
            yield i


for value in my_range_gen(3, 8):
    print(value)

for value in my_range_gen(5):
    print(value)

for value in my_range_gen(7, 2):
    print(value)
print('End')