match_1 = list(map(int,input().split(':')))
match_2 = list(map(int,input().split(':')))
sign = int(input())

total_1 = match_1[0] + match_2[0]
total_2 = match_1[1] + match_2[1]
total_loss = total_2 - total_1

if total_1 > total_2:
    print(0)
elif total_1 == total_2 == 0:
    print(1)
elif total_1 == total_2:
    if sign == 1:
        if match_2[0] > match_1[1]:
            print(0)
        elif match_2[0] == match_1[1]:
            print(1)
        else:
            print(1)
    elif sign == 2:
        if match_1[0] > match_2[1]:
            print(0)
        elif match_1[0] == match_2[1]:
            print(1)
        else:
            print(1)

elif total_1 < total_2:
    if sign == 1:
        if total_loss + match_2[0] == match_1[1]:
            print(total_loss + 1)
        elif total_loss + match_2[0] > match_1[1]:
            print(total_loss)
        elif total_loss + match_2[0] < match_1[1]:
            print(total_loss + 1)

    if sign == 2:
        if match_1[0] > match_2[1]:
            print(total_loss)
        else:
            print(total_loss + 1)
