month_li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# year0 month1 day2 hour3 min4 sec5
# ввод данных
li_begin = input().split()
li_end = input().split()

# расчет начальной точки в секундах
# год в секундах
year_sec_begin =int(li_begin[0]) * sum(month_li) * 24 * 60 * 60
#месяц в секундах
month_sec_begin = 0
for i in range(int(li_begin[1])-1):
    month_sec_begin += month_li[i] * 24 * 60 * 60
# дни в секундах + часы в секундах + минуты в секундах +секунды
day_hour_min_sec_begin = int(li_begin[2]) * 24 * 60 * 60 + int(li_begin[3]) * 60 * 60 + int(li_begin[4]) * 60 + int(li_begin[5])
#точка_начала ( вся дата выраженная в секундах)
begin_sec = year_sec_begin + month_sec_begin + day_hour_min_sec_begin

# расчет конечной точки в секундах
# год в секундах
year_sec_end =sum(month_li) * int(li_end[0]) * 24 * 60 * 60
#месяц в секундах
month_sec_end = 0
for i in range(int(li_end[1])-1):
    month_sec_end += month_li[i] * 24 * 60 * 60
# дни в секундах + часы в секундах + минуты в секундах +секунды
day_hour_min_sec_end = int(li_end[2]) * 24 * 60 * 60 + int(li_end[3]) * 60 * 60 + int(li_end[4]) * 60 + int(li_end[5])
#точка_начала ( вся дата выраженная в секундах)
end_sec = year_sec_end + month_sec_end + day_hour_min_sec_end

# расчет секунда между датами
period = end_sec - begin_sec
days_passed = period // 60 //60 // 24
#sec_passed
sec_passed = period - days_passed * 24 * 60 * 60
print(days_passed,sec_passed, sep=' ')


