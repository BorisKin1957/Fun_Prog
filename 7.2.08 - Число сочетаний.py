def get_combin(n, k):
    if k == 0:
        return 1
    elif k == n:
        return 1
    return get_combin(n - 1, k - 1) + get_combin(n - 1, k)


print(get_combin(6, 3))
print(get_combin(10, 7))