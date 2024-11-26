'''Условный опреатор в функции lambda

скидка должна быть только для тех товаров, стоимость которых больше 50'''


sale_lambda = lambda prise: prise * 0.9 if prise > 50 else prise

print(sale_lambda(50.0))
print(sale_lambda(60.0))