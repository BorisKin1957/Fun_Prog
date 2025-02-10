def gen_fibonacci_numbers(n):
    one, two = 0, 1
    for i in range(n):
        result = one + two
        yield result
        one, two = result, one


for i in gen_fibonacci_numbers(10):
    print(i)

