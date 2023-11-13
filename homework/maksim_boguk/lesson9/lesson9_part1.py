import datetime

time_now = datetime.datetime.strptime("01/15/2023 12:05:33", "%m/%d/%Y %H:%M:%S")
print('Текущий месяц:', time_now.month)
print(time_now.strftime('%d.%m.%y, %H:%M'))
