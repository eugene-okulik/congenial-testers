"""
Документация по использованию скрипта для поиска ошибок в логах

Описание:
Этот скрипт предназначен для анализа логов и поиска
в них сообщений об ошибках или других интересующих строк.

Использование:
Скрипт запускается из командной строки с различными аргументами для фильтрации логов.
- -f, --file: Указание пути к файлу лога.
- -d, --dir: Указание папки с файлами логов.
- -t, --date: Фильтрация сообщений по определенной дате (формат YYYY-MM-DD).
- -b, --before: Фильтрация сообщений до указанной даты.
- -a, --after: Фильтрация сообщений после указанной даты.
- -s, --text: Поиск текста в сообщениях.
- -o, --output: Формат вывода результатов ('brief' для краткого и 'full' для полного).

Примеры команд:
1. Поиск сообщений с определенным текстом в одном файле логов:
   python script.py --file path/to/logfile.log --text "ошибка"

2. Поиск сообщений до определенной даты в папке с логами:
   python script.py --dir path/to/logfiles --before 2021-12-31

3. Поиск сообщений с определенным текстом и вывод только первых 300 символов каждого сообщения:
   python script.py --file path/to/logfile.log --text "ошибка" --output brief

4. Поиск сообщений в определенный день:
   python script.py --file path/to/logfile.log --date 2021-12-31

5. Поиск сообщений после определенной даты в файле:
   python script.py --file path/to/logfile.log --after 2021-01-01

Заметки:
Для помощи можно использовать команду: python script.py --help
"""

import argparse
import datetime
import os
from typing import Generator


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Поиск ошибок в логах")
    parser.add_argument("-f", "--file", dest="file", type=str, help="Файл лога")
    parser.add_argument(
        "-d", "--dir", dest="dir", type=str, help="Папка с файлами логов"
    )
    parser.add_argument(
        "-t", "--date", dest="date", type=str, help="Дата сообщения (YYYY-MM-DD)"
    )
    parser.add_argument(
        "-b",
        "--before",
        dest="before",
        type=str,
        help="Дата до которой искать сообщения (YYYY-MM-DD)",
    )
    parser.add_argument(
        "-a",
        "--after",
        dest="after",
        type=str,
        help="Дата после которой искать сообщения (YYYY-MM-DD)",
    )
    parser.add_argument(
        "-s",
        "--text",
        dest="text",
        type=str,
        help="Текст, по которому искать сообщения",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        type=str,
        default="full",
        help="Формат вывода результатов: 'brief' или 'full'",
    )
    return parser.parse_args()


def parse_date(date_str: str) -> datetime.datetime:
    return datetime.datetime.strptime(date_str, "%Y-%m-%d")


def get_blocks(filename: str) -> Generator[str, None, None]:
    try:
        with open(filename, "r") as f:
            for line in f:
                yield line
    except IOError:
        print(f"Ошибка чтения файла: {filename}")


def filter_messages(
    messages: Generator[str, None, None], args: argparse.Namespace
) -> Generator[str, None, None]:
    for message in messages:
        message_date = message.split(",")[0]
        if args.date and args.date not in message_date:
            continue
        if args.before and parse_date(message_date) >= parse_date(args.before):
            continue
        if args.after and parse_date(message_date) <= parse_date(args.after):
            continue
        if args.text and args.text not in message:
            continue
        yield message


def extract_context(message: str, keyword: str, context_length: int = 150) -> str:
    index = message.find(keyword)
    if index != -1:
        start = max(index - context_length, 0)
        end = min(index + len(keyword) + context_length, len(message))
        return message[start:end]
    return message


def print_results(
    messages: Generator[str, None, None], args: argparse.Namespace
) -> None:
    for message in messages:
        if args.text:
            message = extract_context(message, args.text)
            if not message.strip():  # Проверяем, не является ли строка пустой
                continue

        if args.output == "brief":
            print(message[:300])
        elif args.output == "full":
            print(message)
        else:
            print("Неизвестный формат вывода:", args.output)


def process_file(filename: str, args: argparse.Namespace) -> None:
    messages = get_blocks(filename)
    filtered_messages = filter_messages(messages, args)
    print_results(filtered_messages, args)


def process_directory(directory: str, args: argparse.Namespace) -> None:
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            process_file(filepath, args)


def main() -> None:
    args = get_args()
    if args.file:
        process_file(args.file, args)
    elif args.dir:
        process_directory(args.dir, args)


if __name__ == "__main__":
    main()
