n1 = int(input())
set_1 = set(map(int, input().split()))

n2 = int(input())
set_2 = set(map(int, input().split()))


n3 = int(input())
set_3 = set(map(int, input().split()))

inters_1 = set.intersection(set_1, set_2)
inters_2 = set.intersection(set_2, set_3)
inters_3 = set.intersection(set_1, set_3)

myset1 = inters_1 | inters_2 | inters_3
result = sorted(list(myset1))
print(*result)


if __name__ == '__main__':
    print(inters_1)
    print(inters_2)
    print(inters_3)

