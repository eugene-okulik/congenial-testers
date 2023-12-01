import datetime

time_now = datetime.datetime.strptime("01/15/2023 12:05:33", "%m/%d/%Y %H:%M:%S")
month_name = time_now.strftime("%B")
print('Текущий месяц:', month_name)
print(time_now.strftime('%d.%m.%y, %H:%M'))
