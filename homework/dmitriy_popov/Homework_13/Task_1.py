import os
import datetime


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
okulik_file_path = os.path.join(homework_path, 'eugeny_okulik', 'hw_13', 'data.txt')
print(okulik_file_path)


def read_file(file_path):
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file(okulik_file_path):
    line_with_date = data_line.split(" - ")
    number_in_line, date_in_line = line_with_date[0].split(". ")
    python_date = datetime.datetime.strptime(date_in_line, '%Y-%m-%d %H:%M:%S.%f')

    if number_in_line == '1':
        print(f'Через неделю от даты: "{date_in_line}" будет {python_date + datetime.timedelta(weeks=1)}')
    elif number_in_line == '2':
        print(f'День недели у даты: "{date_in_line}" будет - {python_date.strftime('%A')}')
    else:
        now = datetime.datetime.now()
        print(f'Дата: "{date_in_line}" была {(datetime.datetime.now() - python_date).days} дней назад')


read_file(okulik_file_path)






