def get_sort_lines(lines_list):
    new = sorted(lines_list, key=lambda x: (abs(x[1] - x[0]), x[0], x[1]))# сортировка отрезков
    return new


lines = [(-4, 4), (2, 3), (5, 9), (-1, -3) ]
print(get_sort_lines(lines))

print()

lines = [(5, 6), (5, 4), (1, 0), (0, -1), (1, 2), (2, 1)]
print(get_sort_lines(lines))