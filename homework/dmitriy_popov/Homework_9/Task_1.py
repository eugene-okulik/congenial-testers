import datetime


my_time = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(my_time, '%b %d, %Y - %H:%M:%S')
full_month = python_date.strftime('%B')
format_date = python_date.strftime('%d.%m.%Y, %H:%M')

print(f'Полное название месяца: {full_month}')
print(f'Дата: {format_date}')
