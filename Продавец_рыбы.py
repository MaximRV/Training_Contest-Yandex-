li = list(map(int, input().split()))
n = li[0]
k = li[1]
li_days = list(map(int, input().split()))

max_profit = 0

for i in range(n):
    if k >= (n - i - 1):
        for j in range(1, (n - i - 1) + 1):
            if li_days[i + j] - li_days[i] > max_profit:
                max_profit = li_days[i + j] - li_days[i]
    else:
        for j in range(1, k + 1):
            if li_days[i + j] - li_days[i] > max_profit:
                max_profit = li_days[i + j] - li_days[i]

print(max_profit)
