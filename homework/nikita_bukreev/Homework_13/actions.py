import os
import datetime
from functions import read_file, find_date


# base_path = os.path.dirname(__file__)
# home_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# need_file_path = os.path.join(home_path, 'eugeny_okulik', 'hw_13', 'data.txt')
need_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'eugeny_okulik', 'hw_13', 'data.txt')

for string in read_file(need_file_path):
    if string.startswith('1'):
        find_need_date = find_date(string)
        need_date = find_need_date + datetime.timedelta(weeks=1)
        print(f'Дата, которая позже на неделю заданной даты ("{find_need_date}"), будет равна "{need_date}"')
    elif string.startswith('2'):
        find_need_date = find_date(string)
        need_date = datetime.datetime.strftime(find_need_date, '%A')
        print(f'"{find_need_date}" это был(а) {need_date}')
    elif string.startswith('3'):
        find_need_date = find_date(string)
        need_date = datetime.datetime.now().date() - find_need_date.date()
        print(f'Дата "{find_need_date}" была ровно {str(need_date)[0:3]} дней назад')
