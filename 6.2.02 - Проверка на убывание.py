num = list(map(int, input().split()))

print(all([num[i + 1] < num[i] for i in range(len(num) - 1)]))

