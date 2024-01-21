import os
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'be_BY.utf8')

base_path = os.path.dirname(__file__)

homework_path = os.path.dirname(os.path.dirname(base_path))
eugeny_file_path = os.path.join(homework_path, 'eugeny_okulik', 'hw_13', 'data.txt')
print(eugeny_file_path)

with open(eugeny_file_path) as eugeny_file:
    print(eugeny_file.read())


def read_file():
    with open(eugeny_file_path, 'r') as data_file:
        # print(data_file)
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    data_line = data_line.split(' - ')
    read_date = datetime.datetime.strptime(data_line[0].split('. ')[1], '%Y-%m-%d %H:%M:%S.%f')
    if data_line[0].split('. ')[0] == '1':
        print(f'На тыдзень пазней:', read_date + datetime.timedelta(weeks=1))
    elif data_line[0].split('. ')[0] == '2':
        print(f'Гэта быў дзень тыдню -', read_date.strftime("%A"))
    else:
        print(f'Дата:', read_date, 'была', (datetime.datetime.now() - read_date).days, 'дні таму')