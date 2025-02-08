def gen_arithmetic_progression(start, step):
    while step:
        yield start
        start += step


count = 1
for value in gen_arithmetic_progression(0, 7):
    print(value)
    count += 1
    if count > 5:
        break

count = 8
for value in gen_arithmetic_progression(105, -5):
    print(value)
    count -= 1
    if count == 0:
        break