
def filter_collection(f, l):
    if  isinstance(l, str):
        return ('').join([i for i in l if f(i)])
    elif  isinstance(l, list):
        return [i for i in l if f(i)]
    elif  isinstance(l, tuple):
        return tuple([i for i in l if f(i)])
    elif  isinstance(l, set):
        return set([i for i in l if f(i)])
    elif  isinstance(l, dict):
        return {k: v for k, v in l.items() if f(k)}
    else:
        return None




print(filter_collection(lambda x: x not in 'aeiou', 'I never heard those lyrics before'))

print()

def is_even(num):
    return num % 2 == 0

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers = filter_collection(is_even, numbers)
print(even_numbers)

print()

def is_positive(num):
    return num > 0

numbers = [-1, 2, -3, 4, 5, -6, 7, -8, -9, 10]
positive_numbers = filter_collection(is_positive, numbers)
print(positive_numbers)