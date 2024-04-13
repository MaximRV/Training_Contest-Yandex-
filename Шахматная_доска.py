n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))
total_1 = 0
total_2 = 0

count = 0
for i in range(n - 1):
    for j in range(1, (n - i - 1) + 1):
        if li[i][0] == li[i + j][0] and abs(li[i][1] - li[i + j][1]) == 1:
            count += 1
        elif li[i][1] == li[i + j][1] and abs(li[i][0] - li[i + j][0]) == 1:
            count += 1

print(n * 4 - count * 2)
