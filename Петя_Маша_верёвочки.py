n = int(input())
li = list(map(int,input().split()))

max_li = max(li)
s_li = sum(li) - max_li
if s_li< max_li:
    print(max_li - s_li)
elif s_li >= max_li:
    print(sum(li))