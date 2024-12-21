def double_it(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper


@double_it
def multiply(num1, num2):
    return num1 * num2

res = multiply(9, 4) # произведение 9*4=36, но декоратор double_it удваивает это значение
print(res)

print()

@double_it
def get_sum_kwargs_values(**kwargs):
    return sum(kwargs.values())


print(get_sum_kwargs_values(a=4, b=5, c=7))
print(get_sum_kwargs_values(a=4, b=5, d=3, t=6, r=8))