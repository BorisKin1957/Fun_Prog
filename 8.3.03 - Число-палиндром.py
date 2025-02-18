def is_palindrome():
    word = yield
    while True:
        word = str(word)
        word = yield word == word[::-1]

coro = is_palindrome()
next(coro)
print(coro.send(1771))
print(coro.send(987))
print(coro.send(1))
print(coro.send(1234321))

print()

coro = is_palindrome()
next(coro)
for num in [1, 12, 123, 1221, 45654, 999]:
    print(coro.send(num))