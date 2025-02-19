def lstrip(lst, item):
    while lst and lst[0] == item:
        lst.pop(0)


data = [0, 0, 1, 0, 2, 3]
print(data)
print(lstrip(data, 0))
print(data)