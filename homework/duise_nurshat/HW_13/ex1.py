import os
from datetime import datetime, timedelta

# возвращает то место где ты находишься
base_path = os.path.dirname(__file__)
# ищем где находится папка duise_nurshat(поднимаемся на две папки выше)
file_path = os.path.dirname(os.path.dirname(base_path))
# находим нужный файл
needed_file_path = os.path.join(file_path, 'eugeny_okulik', 'hw_13', 'data.txt')

# читать файл
with open(needed_file_path, 'r', encoding='utf-8') as homework_file:
    for line in homework_file:
        new_line = line.split(' - ')
        index = str(new_line[0].split('. ')[0])
        date = str(new_line[0].split('. ')[1])
        date_time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        if index == '1':
            print(date_time + timedelta(weeks=1))
        elif index == '2':
            print(date_time.weekday())
        elif index == '3':
            print(datetime.now() - date_time)
