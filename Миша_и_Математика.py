n = int(input())
li = list(map(int, input().split()))

result = []
f = []

if li[0] % 2 != 0:
    f.append(1)
else:
    f.append(2)

for i in range(n - 1):
    if f[len(f)-1] == 1 and li[i+1] % 2 != 0:
        result.append('x')
        f.append(1)
    elif f[len(f)-1] == 1 and li[i+1] % 2 == 0:
        result.append('+')
        f.append(1)
    elif f[len(f)-1] == 2 and li[i+1] % 2 == 0:
        result.append('x')
        f.append(2)
    elif f[len(f)-1] == 2 and li[i+1] % 2 != 0:
        result.append('+')
        f.append(1)

x = ''.join(result)
print(x)
