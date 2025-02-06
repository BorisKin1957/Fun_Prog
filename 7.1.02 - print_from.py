def print_from(n):
    if n > 0:
        print(n)
        print_from(n - 1)




print_from(7)