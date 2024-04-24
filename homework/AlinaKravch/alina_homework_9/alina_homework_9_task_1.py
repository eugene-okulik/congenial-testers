import datetime


date = 'Jan 15, 2023 - 12:05:33'
py_date = datetime.datetime.strptime(date, '%b %d, %Y - %X')
print(py_date)
print(py_date.strftime('%d.%m.%Y, %H:%M'))
