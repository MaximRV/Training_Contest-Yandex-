n = int(input())
myset = {}
li = []
for _ in range(n):
    m = int(input())
    s = input().split()
    for i in s:
        if i in myset:
            myset[i] += 1
        else:
            myset[i] = 1

for i in myset:
    if myset[i] == n:
        li.append(i)
print(len(li))
print(*sorted(li))
