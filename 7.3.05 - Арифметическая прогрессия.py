def get_arith_progression(n, result=1):
    if n == 1:
        return result
    return get_arith_progression(n - 1, result + 7)


print(get_arith_progression(2))
print(get_arith_progression(3))
print(get_arith_progression(1))
