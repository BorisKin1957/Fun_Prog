def summa(n):
    if n == 1:
        return n
    return n + summa(n-1)


print(summa(4))