import os
import argparse
import datetime
from colorama import Fore, Style, init


def parse_args():
    parser = argparse.ArgumentParser(
        prog='Log Analyzer by Bukreev',
        description='Analyze log files with your filter',
        epilog=f'''Welcome and enjoy!\n
        Example usage: {os.linesep}
        python3 args.py ../../eugeny_okulik/data/logs/rpe-api-error.2022-02-03.0.log - прочитает файл \n
        python3 args.py ../../eugeny_okulik/data/logs/ - прочитает все файлы в диерктории \n
        python3 args.py ../../eugeny_okulik/data/logs/ "/2024-01-01 00:00:00.000/" - прочитает все файлы в диерктории
        и отфильтрует по дате \n
        python3 args.py ../../eugeny_okulik/data/logs/rpe-api-error.2022-02-03.0.log  -t "kek lol" - найти только
        текст \n
        python3 args.py .../../eugeny_okulik/data/logs/rpe-api-error.2022-02-03.0.log  -t "kek lol" -u "arbidol" -
        найти текст и исключить с другим текстом \n
        python3 args.py ../../eugeny_okulik/data/logs/rpe-api-error.2022-02-03.0.log  -t "kek lol" -u "arbidol" -f -
        найти текст и исключить текст и вывести необрезанный лог \n
        python3 args.py ../../eugeny_okulik/data/logs/rpe-api-error.2022-02-03.0.log  -u "kek lol" - вывести лог в
        котором нет текста \n
        P.S на маке у меня не получилось сделать так, чтобы символ \\n делал переход на следующуб строку((''')
    parser.add_argument('file_path', type=str, help='Path to file or directory')
    parser.add_argument('-d', '--date', type=str, help='''Datetime for search: less then:
    "../2024-01-01 00:00:00.000", more than: "2024-01-01 00:00:00.000/..",
    from - to: "2024-01-01 00:00:00.000/2024-01-01 00:00:00.000", exact: "/2024-01-01 00:00:00.000/"''')
    parser.add_argument('-t', '--text', type=str, help='Text for search')
    parser.add_argument('-u', '--unwanted', type=str, help='A text to filter out logs')
    parser.add_argument('-f', '--full', help='Returns full log', action='store_true')
    args = parser.parse_args()

    file_path = args.file_path
    date = args.date
    text = args.text
    unwanted = args.unwanted
    full = args.full
    return file_path, date, text, unwanted, full


def starts_with_datetime(string, format_datetime="%Y-%m-%d %H:%M:%S.%f"):
    try:
        datetime.datetime.strptime(string[:23], format_datetime)
        return True
    except ValueError:
        return False


def read_file(file_path):
    absulut_path = os.path.abspath(file_path)
    data = {}
    if os.path.isdir(absulut_path):
        for file in os.listdir(absulut_path):
            file_path = os.path.join(absulut_path, file)
            with open(file_path, 'r') as f:
                for line in f.readlines():
                    if starts_with_datetime(line):
                        data[line[:23]] = line
                    else:
                        last_key = list(data.keys())[-1]
                        data[last_key] += f' {line}'
    elif os.path.isfile(absulut_path):
        with open(absulut_path, 'r') as file:
            for line in file.readlines():
                if starts_with_datetime(line):
                    data[line[:23]] = line
                else:
                    last_key = list(data.keys())[-1]
                    data[last_key] += f' {line}'
    else:
        print('Ощибка при поиске файла или каталога, проверьте указанный путь!')
    return data


def date_parser(date):
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    try:
        delitel_index = date.index('/')
    except ValueError:
        return print('Формат даты не подходит, отсутсвтует /, смотри описание.')

    try:
        if delitel_index == 2:
            date_to = datetime.datetime.strptime(date[3:], date_format).strftime(date_format)[:-3]
            flag = 'date_to'
            return flag, date_to
        elif delitel_index == 23:
            if date[24] == '.':
                date_from = datetime.datetime.strptime(date[:-3], date_format).strftime(date_format)[:-3]
                flag = 'date_from'
                return flag, date_from
            elif date[24] == '2':
                date_to = datetime.datetime.strptime(date[:23], date_format).strftime(date_format)[:-3]
                date_from = datetime.datetime.strptime(date[24:], date_format).strftime(date_format)[:-3]
                flag = 'date_from_to'
                return flag, date_to, date_from
        elif delitel_index == 0 and date[-1] == '/':
            date_one = datetime.datetime.strptime(date[1:-1], date_format).strftime(date_format)[:-3]
            flag = 'date_one'
            return flag, str(date_one)
        else:
            print('Формат даты не подходит, смотри описание.')
    except ValueError:
        return print("Допущена ошибка в формате даты, смотри описание.")


def find_date(data, flag, *user_date):
    filtered_dates = []
    if len(user_date) == 1:
        if flag == 'date_to':
            user_date = datetime.datetime.strptime(str(user_date[0]), '%Y-%m-%d %H:%M:%S.%f')
            filtered_dates = [date for date in data if
                              datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') <= user_date]
        elif flag == 'date_from':
            user_date = datetime.datetime.strptime(str(user_date[0]), '%Y-%m-%d %H:%M:%S.%f')
            filtered_dates = [date for date in data if
                              datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') >= user_date]

        elif flag == 'date_one':
            user_date = datetime.datetime.strptime(str(user_date[0]), '%Y-%m-%d %H:%M:%S.%f')
            filtered_dates = [date for date in data if
                              datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') == user_date]
        else:
            print('Что-то не так с датой или флагом')
    elif len(user_date) == 2:
        if flag == 'date_from_to':
            user_date_from = datetime.datetime.strptime(str(user_date[0]), '%Y-%m-%d %H:%M:%S.%f')
            user_date_to = datetime.datetime.strptime(str(user_date[1]), '%Y-%m-%d %H:%M:%S.%f')
            filtered_dates = [date for date in data if
                              user_date_from <= datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
                              <= user_date_to]
        else:
            print('Что-то не так с датами или флагом')
    else:
        print(f'Функция нахождения даты не справилась с работой {user_date}')
    return filtered_dates


def filter_by_date(data, dates):
    filtered_dict = {key: value for key, value in data.items() if key in dates}
    return filtered_dict


def find_text(data, text=None, unwanted=None, full=False):
    result = {}
    for key, value in data.items():
        if (text is None or text in value) and (unwanted is None or unwanted not in value):
            if full is True:
                result[key] = value
            else:
                if text is not None:
                    start_index = max(value.find(text) - 150, 0)
                    end_index = min(value.find(text) + len(text) + 150, len(value))
                    result[key] = value[start_index:end_index]
                else:
                    result[key] = value[:300]
    return result


def print_colored_dict(d, word_to_highlight=None):
    init()

    colored_dict = {}
    key_color = Fore.YELLOW
    for key, value in d.items():
        colored_key = f"{key_color}{key}{Style.RESET_ALL}"
        if word_to_highlight is not None:
            parts = value.split(word_to_highlight)
            colored_value = f"{Fore.RED}{word_to_highlight}{Style.RESET_ALL}".join(parts)
        else:
            colored_value = value
        colored_dict[colored_key] = colored_value

    return colored_dict
