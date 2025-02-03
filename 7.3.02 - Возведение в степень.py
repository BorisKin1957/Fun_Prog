def power(a: int, n: int) -> int:
    if n == 1:
        return a
    return a * power(a, n - 1)

print(power(2, 3))
print(power(2, 5))
print(power(2, 7))
print(power(3, 4))
