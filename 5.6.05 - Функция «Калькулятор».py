def calculate(x, y, operation='a'):
    addition = lambda x, y: x + y
    subtraction = lambda x, y: x - y
    division = lambda x, y: x / y if y != 0 else 'На ноль делить нельзя!'
    multiplication = lambda x, y: x * y


    if operation == 'a':
        print(addition(x, y))
    elif operation =='s':
        print(subtraction(x, y))
    elif operation == 'm':
        print(multiplication(x, y))
    elif operation == 'd':
        print(division(x, y))
    else:
        print('Ошибка. Данной операции не существует.')

calculate(10, 4, 's')
calculate(10, 0, 'd')
calculate(10, 4, 'w')
calculate(1, 2, 'a')
calculate(3, 1, 'd')