def factorial(n, cashe = {1: 1}, result = 1):
    if n in cashe:
        print(f'Get from cache value factorial({n})')
        return cashe[n]
    else:
        for i in range(1, n + 1):
            result *= i
        cashe[n] = result
    return result


print(factorial(5))
print(factorial(6))
print(factorial(5))