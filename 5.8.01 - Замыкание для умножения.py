def multiply(num1):# Замыкание
    def inner(num2):
        return num2 * num1
    return inner


f_2 = multiply(2)
print("Умножение 2 на 5 =", f_2(5))
print("Умножение 2 на 15 =", f_2(15))