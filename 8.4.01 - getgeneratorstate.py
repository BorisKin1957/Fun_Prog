from inspect import getgeneratorstate


def my_coro(a):
    print(f'Запускаем корутину со значением a={a}')
    while True:
        b = yield a
        print(f'Получено значение b={b}')
        c = yield a + b
        print(f'Получено значение c={c}')


coro = my_coro(7)
print(getgeneratorstate(coro))
next(coro)
print(getgeneratorstate(coro))
print(coro.send(23))
print(getgeneratorstate(coro))
coro.send(100)

coro.close()
print(getgeneratorstate(coro))