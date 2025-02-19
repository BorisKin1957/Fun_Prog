def my_func(collection, n):
    data = collection.copy()
    for i in range(1, n + 1):
        data.append(i)
    return data


a = [10, 20, 30]
res = my_func(a, 3)
print(a)
print(res)