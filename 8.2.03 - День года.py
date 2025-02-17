week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def print_week(d):

    k, m = 1, 300 % 7
    for i in range(d // 7):
        for j in range(7):
            print((k + j, week[j]))
        k += 7

    for i in range(d % 7):
        print((k + i, week[i]))


print_week(10)