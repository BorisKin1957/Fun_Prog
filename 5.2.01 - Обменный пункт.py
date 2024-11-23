def convert(curr_1, curr_2, quantity):
    if curr_1 == 'USD':
        return round(quantity * exchange_rates[curr_2], 2)
    else:
        return round(quantity / exchange_rates[curr_1], 2)


exchange_rates = {
    "USD": 1.0,
    "EUR": 0.861775,
    "GBP": 0.726763,
    "INR": 75.054725,
    "AUD": 1.333679,
    "CAD": 1.237816,
    "SGD": 1.346851,
}



currency = convert("USD", "EUR", 100)
print(currency)

currency = convert("USD", "AUD", 1000)
print(currency)

currency = convert("EUR", "USD", 100)
print(currency)

currency = convert("GBP", "USD", 100)
print(currency)