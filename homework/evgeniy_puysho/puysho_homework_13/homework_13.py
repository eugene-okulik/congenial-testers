import os
from _datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
hm_path = os.path.dirname(os.path.dirname(base_path))
hw_file_path = os.path.join(hm_path, 'eugeny_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(hw_file_path, 'r') as data_file:
        for line in data_file:
            line_with_date = line.strip().split(" - ")
            index = str(line_with_date[0].split('. ')[0])
            date = str(line_with_date[0].split('. ')[1])
            date_object = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            if index == '1':
                print(f'Исходная дата: {date_object}, '
                      f'Новая дата (после добавления недели): '
                      f'{date_object + timedelta(weeks=1)}'
                      )
            elif index == '2':
                print(f'Исходная дата: {date_object}, День недели: {date_object.weekday()}')
            elif index == '3':
                current_date = datetime.now()
                days_ago = (current_date - date_object).days
                print(f'Исходная дата: {date_object} была {days_ago} дней назад')


read_file()
