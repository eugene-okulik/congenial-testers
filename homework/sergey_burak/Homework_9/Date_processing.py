# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:
# 1. Распечатайте полное название месяца из этой даты
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"

import datetime

my_time = 'Jan 15, 2023 - 12:05:33'
python_time = datetime.datetime.strptime(my_time, '%b %d, %Y - %X')
# month = python_time.strftime('полное название месяца: %B')
# new_format_time = python_time.strftime('%d.%m.%Y, %H:%M')
print(f'Питоновский формат: {python_time}')
print(python_time.strftime('полное название месяца: %B'))
print(python_time.strftime('%d.%m.%Y, %H:%M'))
