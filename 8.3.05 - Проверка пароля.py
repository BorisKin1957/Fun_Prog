from sympy.strategies.branch import yieldify


def check_password():
    password = yield
    while True:
        password = yield (len(password) > 9
                          and any(c.isdigit() for c in password)
                          and any(c.isupper() for c in password)
                          and any(c in '!@#$%' for c in password))


coro = check_password()
next(coro)
print(coro.send('qwerty'))
print(coro.send('qwertyuiop'))
print(coro.send('qwerty1234'))
print(coro.send('qwerty123!'))
print(coro.send('qwerty123?'))
print(coro.send('Qwerty123?'))
print(coro.send('Qwerty123@'))