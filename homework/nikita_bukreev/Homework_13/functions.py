import datetime
import re


def read_file(file_path):
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


def find_date(line):
    date_find = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+').findall(line)
    python_date_format = '%Y-%m-%d %H:%M:%S.%f'
    found_date = datetime.datetime.strptime(date_find[0], python_date_format)
    return found_date
