def find_keys(**kwargs):
    result = sorted([key for key, value in kwargs.items() if isinstance(value, (list, tuple))], key=lambda x: x.lower())
    return result


print(find_keys(marks=[4, 5], name='Ashle', surname='Brown', age=20, Also=(1, 2)))
print()
print(find_keys(t=[4, 5], w=[5, 3], A=(3, 2), a={2, 3}, b=[4]))
print()
print(find_keys(marks=[4, 5], ashle=[5], surname='Brown', age=20, Also=(1, 2)))
print()
print(find_keys(At=[4], awaited=(3,), aDobe=[5]))