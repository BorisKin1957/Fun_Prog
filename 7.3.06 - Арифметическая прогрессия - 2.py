def get_arith_progression(a, d, n):
    if n == 1:
        return a
    return get_arith_progression(a + d, d, n - 1)


print(get_arith_progression(4, 2, 3))
print(get_arith_progression(10, -3, 5))
print(get_arith_progression(100, -8, 11))