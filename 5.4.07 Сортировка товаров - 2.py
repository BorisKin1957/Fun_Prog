def print_goods(models_list):
    result = sorted(models_list, key=lambda x: (-float(x.split(':')[1]), x.split(':')[0].lower()))
    for item in result:
        prise = float(item.split(':')[1])
        model = item.split(':')[0]
        print(f"{prise:.2f} - {model}")


data = [
    'Sony PlayStation 5: 46000',
    'Телевизор QLED Samsung QE65Q60TAU: 87090',
    'Смартфон Samsung Galaxy A11: 10000',
    'Планшет Samsung Galaxy Tab S6: 26600',
]

print_goods(data)

print()

data = [
    'Sony PlayStation 5: 46000.5',
    'Телевизор QLED Samsung QE65Q60TAU: 87090',
    'Samsung Galaxy s23: 46000.5',
    'siemens eq.6 plus s100: 46000.5',
    'Samsung Galaxy Tab S6: 46000.5',
]
print_goods(data)

print()

data = [
    'a: 1',
    'aa: 2',
    'aA: 3',
    'Aa: 4',
    'Aa: 5',
    'AA: 5',
    'aa: 5',
    'aA: 5',
]
print_goods(data)