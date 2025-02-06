def luhn_algorithm(number):
    n = str(number)[::-1]
    l1 = [int(n[i]) for i in range(0, 16, 2)]
    l2 = [int(n[i]) for i in range(1, 16, 2)]
    l3 = map(lambda x: x * 2 if x * 2 < 10 else x * 2 - 9, l2)
    return (sum(l3) + sum(l1)) % 10 == 0


print(luhn_algorithm(3942682966937054))
print(luhn_algorithm(2553514623369426))
print(luhn_algorithm(1217040151414995))
print(luhn_algorithm(2146133934667114))
print(luhn_algorithm(4111111111111111))
