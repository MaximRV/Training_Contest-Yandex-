li = list(map(int, input().split()))
profit = li[0]
shareholders = li[1]
days = li[2]

profit_all = 0
count = 0
for i in range(10):
    if (profit * 10 + i) % shareholders == 0:
        profit = (profit * 10 + i)
        profit_all = str(profit) + '0' * (days - 1)
        print(profit_all)
        break
    else:
        count += 1

if count == 10:
    print(-1)
