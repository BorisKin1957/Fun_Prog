call_stack = []

def quick_power(a, n):
    call_stack.append((a, n))
    print(f'State: a={a}, n={n}')
    if n == 0:
        return 1
    if n % 2:
        result = a * quick_power(a, n - 1)
    else:
        result = quick_power(a, n // 2) ** 2
    call_stack.pop()

    return result


print(quick_power(3, 4))
print(quick_power(2, 24))
print(quick_power(2, 5))