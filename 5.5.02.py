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

print_goods.is_working = False
print_goods.status = 'Not ready'

print(check_exist_attrs(print_goods, ['is_working', 'status', 'time', 'speed']))