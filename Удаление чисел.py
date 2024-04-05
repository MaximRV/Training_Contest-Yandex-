n = int(input())
line1 = {}
li = sorted(list(map(int, (input().split()))))

for i in li:
    line1[i] = line1.get(i, 0) + 1

value = 0

for i in line1:
    if line1.get(i-1, 0) + line1[i] > value or line1.get(i+1, 0) + line1[i] > value:
        value = max(line1.get(i-1, 0) + line1[i], line1.get(i+1, 0) + line1[i])

print(n - value)