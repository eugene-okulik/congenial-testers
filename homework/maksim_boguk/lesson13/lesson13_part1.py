import os
import datetime

# Заменяем __file__ на путь к текущему файлу
current_dir = os.path.dirname(os.path.abspath(__file__))
hw_dir = os.path.dirname(os.path.dirname(current_dir))
path = os.path.join(hw_dir, 'eugeny_okulik', 'hw_13', 'data.txt')


def read_file(file_path):
    with open(file_path, 'r') as file:
        for data_line in file:
            line_with_date = data_line.strip().split(" - ")
            number_in_line, date_in_line = line_with_date[0].split(". ")
            date_format = '%Y-%m-%d %H:%M:%S.%f' if len(date_in_line) > 10 else '%Y-%m-%d'
            python_date = datetime.datetime.strptime(date_in_line, date_format)

            if number_in_line == '1':
                new_date = python_date + datetime.timedelta(weeks=1)
                print(f'Через неделю от даты: "{date_in_line}" будет {new_date.strftime(date_format)}')
            elif number_in_line == '2':
                print(f'День недели у даты: "{date_in_line}" будет - {python_date.strftime("%A")}')
            elif number_in_line == '3':
                today = datetime.datetime.now()
                days_ago = (today - python_date).days
                print(f'Дата: "{date_in_line}" была {days_ago} дней назад')


read_file(path)
