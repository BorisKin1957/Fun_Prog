def double_fact(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return n * double_fact(n - 2)


print(double_fact(6))
print(double_fact(5))
print(double_fact(2))
print(double_fact(4))
