'''
n - этажей 2
m- квартир на этаже 2
x окон в высоту в каждой квартире 2
y окон в ширину в каждой квартире 2

всего окон в квартире  x * y
m * y длинная 2*2 = 4 '''

'''
2 2 2 2
X000
000X
X000
XX00'''
import math

n,m,x,y = map(int,input().split())
flats = []
for _ in range(n):
    l1 = [[] for _ in range(m)]

    for i in range(x):
        row = input()
        flat_ind = 0
        position_1 = 0
        position_2 = y
        while position_2 <= m*y:
            l1[flat_ind].extend(row[position_1:position_2])
            flat_ind += 1
            position_1 += y
            position_2 += y
    flats.extend(l1)
total = 0
for flat in flats:
    if flat.count('X') >= math.ceil( (x*y)/2):
        total += 1
print(total)




