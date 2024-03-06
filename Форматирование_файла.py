n = int(input())
li = []
for _ in range(n):
    li.append(input())

Sp = 1
Ta = 4
BS = -1
li_2 = []
for i in li:
    if int(i) == 0:
        a2 = 0
    elif  int(i) // 4 != 0:
        a1 = int(i) // 4
        b = int(i) - a1 * 4
        if b == 3 :
            a2 = 2
        elif b == 2:
            a2 = 2
        elif b == 1:
            a2 = 1
        else:
            a2 = 0
        li_2.append(a1 + a2)
    else:
        if int(i) == 3:
            a2 = 2
        elif int(i) == 2:
            a2 = 2
        else:
            a2 = 1
        li_2.append(a2)
print(sum(li_2))

