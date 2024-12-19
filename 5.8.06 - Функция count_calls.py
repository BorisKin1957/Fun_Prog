def count_calls():
    total_calls = 0
    def inner():
        nonlocal total_calls
        total_calls += 1
        inner.total_calls = total_calls
        return inner.total_calls
    if not hasattr(inner, 'total_calls'):
        inner.total_calls = 0
    return inner

counter = count_calls()
counter()
counter()
print(counter.total_calls)
counter()
print(counter.total_calls)

print()

counter1 = count_calls()
counter2 = count_calls()
counter1()
print(counter1.total_calls, counter2.total_calls)
counter1()
counter2()
print(counter1.total_calls, counter2.total_calls)
counter2()
counter2()
print(counter1.total_calls, counter2.total_calls)