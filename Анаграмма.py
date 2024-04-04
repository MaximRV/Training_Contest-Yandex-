line1 = {}
line2 = {}
for i in input():
    if i in line1:
        line1[i] += 1
    else:
        line1[i] = 1

for i in input():
    if i in line2:
        line2[i] += 1
    else:
        line2[i] = 1

if line1 == line2:
    print('YES')
else:
    print('NO')
