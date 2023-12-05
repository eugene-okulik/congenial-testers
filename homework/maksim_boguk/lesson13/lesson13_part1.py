import datetime
import os

current_dir = os.path.dirname(__file__)
hw_dir = os.path.dirname(os.path.dirname(current_dir))
path = os.path.join(hw_dir, 'eugeny_okulik', 'Lesson_13', 'file.txt')
print(path)


# теперь в ошибку не валится но не понимаю как функцию запустить, если через read_file(path или file_path) - падает
# ошибка

def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()  # Удаляем пробелы и символы новой строки в конце
            parts = line.split(' - ')
            date_part = parts[0]

            date_string = date_part.split(' ')[0]

            try:
                date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
            except ValueError:
                print('Неверный формат даты:', date_string)
                continue  # Переходим к следующей строке файла в случае ошибки

            if date_part.startswith('1.'):
                new_date = date + datetime.timedelta(weeks=1)
                print('Новая дата:', new_date.strftime('%Y-%m-%d %H:%M:%S.%f'))
            elif date_part.startswith('2.'):
                print('День недели:', date.strftime('%A'))
            elif date_part.startswith('3.'):
                today = datetime.datetime.now()
                days_ago = (today - date).days
                print('Количество дней между этой датой и сегодняшней:', days_ago)
