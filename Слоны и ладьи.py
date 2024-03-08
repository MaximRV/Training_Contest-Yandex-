li = list(input().strip() for _ in range(8))
rook = 'R'
bishop = 'B'
rook_list = []
bishop_list = []


# поиск местоположения каждой Ладьи и Слона
for i in range(8):
    for j in range(8):
        if li[i][j] == rook:
            rook_list.append([i, j])
        if li[i][j] == bishop:
            bishop_list.append([i, j])

# все возможные ходы Ладьи
R = []
for i in rook_list:
#направление влево
    a = i[0]
    b = i[1]
    while  b >= 0 and b <= 7:
        if [a , b] not in R and [a, b] not in rook_list:
            if [a, b] in bishop_list:
                break
            else:
                R.append([a, b])
                b = b - 1
        else:
            b = b - 1

# направление вправо
    a = i[0]
    b = i[1]
    while b >= 0 and b <= 7:
        if [a, b] not in R and [a, b] not in rook_list:
            if [a, b] in bishop_list:
                break
            else:
                R.append([a, b])
                b = b + 1
        else:
            b = b + 1

# направление вниз
    a = i[0]
    b = i[1]
    while a >= 0 and a <= 7:
        if [a, b] not in R and [a, b] not in rook_list:
            if [a, b] in bishop_list:
                break
            else:
                R.append([a, b])
                a = a + 1
        else:
            a = a + 1

# направление вверх
    a = i[0]
    b = i[1]
    while a >= 0 and a <= 7:
        if [a, b] not in R and [a, b] not in rook_list:
            if [a, b] in bishop_list:
                break
            else:
                R.append([a, b])
                a = a - 1
        else:
            a = a - 1

# все возможные ходы Слона
B = []

#сторона 1

for i in bishop_list:
    a = i[0]
    b = i[1]
    while  a >= 0 and b <= 7:
        if [a , b] not in B and [a, b] not in bishop_list:
            if [a, b] in rook_list:
                break
            elif [a, b] in R:
                a = a - 1
                b = b + 1
                continue
            else:
                B.append([a, b])
                a = a - 1
                b = b + 1
        else:
            a = a - 1
            b = b + 1



    a = i[0]
    b = i[1]
    while  a <= 7 and b >= 0:
        if [a, b] not in B and [a, b] not in bishop_list:
            if [a, b] in rook_list:
                break
            elif [a, b] in R:
                a = a + 1
                b = b - 1
                continue
            else:
                B.append([a, b])
                a = a + 1
                b = b - 1
        else:
            a = a + 1
            b = b - 1

#сторона 2

    a = i[0]
    b = i[1]
    while  a >= 0 and b >= 0:
        if [a, b] not in B and [a, b] not in bishop_list:
            if [a, b] in rook_list:
                break
            elif [a, b] in R:
                a = a - 1
                b = b - 1
                continue
            else:
                B.append([a, b])
                a = a - 1
                b = b - 1
        else:
            a = a - 1
            b = b - 1

    a = i[0]
    b = i[1]
    while  a <= 7 and b <= 7:
        if [a, b] not in B and [a, b] not in bishop_list:
            if [a, b] in rook_list:
                break
            elif [a, b] in R:
                a = a + 1
                b = b + 1
                continue
            else:
                B.append([a, b])
                a = a + 1
                b = b + 1
        else:
            a = a + 1
            b = b + 1

print(64 - len(bishop_list) - len(rook_list) - len(B) - len(R))
