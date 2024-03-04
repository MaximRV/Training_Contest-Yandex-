l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]

l1 = [l1[0] - l1[1]] + [l1[0] + l1[1]]
l2 = [l2[0] - l2[1]] + [l2[0] + l2[1]]

if min(l1[1], l2[1]) < max(l1[0], l2[0]):
    print((max(l1) - min(l1) + 1) + (max(l2) - min(l2) + 1))

else:
        all_l = l1 + l2
        print(max(all_l) - min(all_l) + 1)