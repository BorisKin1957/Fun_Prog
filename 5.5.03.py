def create_attrs(obj, attrs):
    for attr, value in attrs:
        setattr(obj, attr, value)

def check_exist_attrs(obj, attrs):
    result = {}
    for attr in attrs:
        result[attr] = hasattr(obj, attr)
    return result

def print_goods(lst):
    pass


def check_exist_attrs(obj, lst):
    result = {}
    for attr in lst:
        if hasattr(obj, attr):
            result[attr] = True
        else:
            result[attr] = False
    return result

create_attrs(print_goods, [('house', 1), ('level', 3), ('cost', 1000000)])
print(print_goods.house)
print(print_goods.level)
print(print_goods.cost)

print()

def print_goods(lst):
    pass

create_attrs(print_goods, [('is_working', False), ('days', 10), ('status', 'Not ready')])

print(check_exist_attrs(print_goods, ['sort', 'is_working', 'days', 'status', 'upper']))