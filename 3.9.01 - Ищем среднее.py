def calculate_high_low_avg(*args, log_to_console=False):
    average = (max(args) + min(args)) / 2
    if log_to_console:
        return f'high={max(args)}, low={min(args)}, avg={average}\n{average}'
    return average


avg = calculate_high_low_avg(1, 2, 3, 4, 5)
print(avg)

print()
avg = calculate_high_low_avg(1, 2, 3, 4, 5, log_to_console=True)
print(avg)