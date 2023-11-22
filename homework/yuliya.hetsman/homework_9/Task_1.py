import datetime

example_date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(example_date, '%b %d, %Y - %X')
full_name = python_date.strftime('%B')

print(full_name)
print(python_date.strftime('%d.%m.%Y, %H:%M'))
