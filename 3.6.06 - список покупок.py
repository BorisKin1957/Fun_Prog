def print_goods(*args):
    new = [product for product in args if product and isinstance(product, str)]
    if new:
        for i in range(len(new)):
            print(f'{i + 1}. {new[i]}')
    else:
        print('Нет товаров')


print_goods('apple', 'banana', 'orange')
print_goods(1, True, 'Грушечка', '', 'Pineapple')
print_goods(*list('qwerty'))
print_goods([], {}, 1, 2)
print_goods(*list('abc'), 1, 'hello')