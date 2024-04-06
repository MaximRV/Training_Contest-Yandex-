n = list(map(int, (input().split())))
line1 = {}
line2 = {}
li = list(map(int, (input().split())))

for i in range(n[0]):
    line1[li[i]] = line1.get(li[i], 0) + 1
    line2[i + 1] = li[i]

Flag = 'NO'

for i in line1:
   if line1[i] > 1:
      z = [k for k, v in line2.items() if v == i]
      for j in range(len(z) -1):
         if z[j+1] - z[j] <= n[1]:
            Flag = 'YES'
            break


print(Flag)
