k = int(input())
coordinates = []
for _ in range(k):
    a = tuple(map(int,input().split()))
    coordinates.append(a)
coordinates = set(coordinates)
coordinates = list(coordinates)

min_x = coordinates[0][0]
min_y = coordinates[0][1]
max_x = coordinates[0][0]
max_y = coordinates[0][1]

for i in coordinates:
    if i[0] > max_x:
        max_x = i[0]
    if i[0] < min_x:
        min_x = i[0]
    if i[1] > max_y:
        max_y = i[1]
    if i[1] < min_y:
        min_y = i[1]

print(min_x, min_y, max_x, max_y)

