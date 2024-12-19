def create_dict():
    count, result = 0, {}
    def inner(value):
        nonlocal count
        count += 1
        result.setdefault(count, value)
        return result
    return inner

f_1 = create_dict()
print(f_1('privet'))
print(f_1('poka'))
print(f_1([5, 2, 3]))

f2 = create_dict()
print(f2(5))
print(f2(15))