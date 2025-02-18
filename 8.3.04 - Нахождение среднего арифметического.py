def get_average():
    num = yield
    count, total = 0, 0
    while True:
        count += 1
        total += num
        num = yield total / count




coro = get_average()
next(coro)
print(coro.send(10))
print(coro.send(20))
print(coro.send(6))