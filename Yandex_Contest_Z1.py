import string

n = int(input())
li = []
count_symvols = []
count_numbers = []
number_letter = []
final = []

for _ in range(n):
    li.append(input())

for i in li:  # считаем количество уникальных символов в ФИО
    count_s = []
    for j in i:
        if j.isalpha() and j not in count_s:
            count_s.append(j)
    count_symvols.append(len(count_s))

for i in li:  # суммируем цифры даты и месяца рождения
    count_data = 0
    for j in i.split(',')[:-1]:
        if j.isdigit():
            if len(j) == 2:
                a = int(j[0]) + int(j[1])
            else:
                a = int(j[0])
            count_data += int(a)
    count_numbers.append(count_data)

for i in li: # находим номер в алфавите первой буквы фамилии
    x = i.split(',')[0]
    letter_num = string.ascii_uppercase.find(x[0].upper()) + 1
    number_letter.append(letter_num)

[ final.append(hex(count_symvols[i] + count_numbers[i] * 64 + number_letter[i] * 256)) for i in range(n)] # собираем итоговое значение шифра

for i in final: # Финальный вывод с преобразованием формата
    if 1 < len(i[2:]) < 3:
        print('0' + i[2:].upper(), end=' ')
    elif len(i[2:]) == 1:
        print('00' + i[2:].upper(), end=' ')
    else:
        print(i[-3:].upper(), end=' ')


