import argparse
import datetime
import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Файл лога")
    parser.add_argument("-d", "--date", help="Дата сообщения в формате YYYY-MM-DD")
    parser.add_argument("-t", "--text", help="Текст сообщения")
    parser.add_argument("-l", "--limit", help="Лимит вывода сообщений", type=int, default=300)
    return parser.parse_args()


def merge_dicts(dict1, dict2):
    merged_dict = {}
    for key, value in dict1.items():
        merged_dict[key] = value
    for key, value in dict2.items():
        merged_dict[key] = value
    return merged_dict


def get_file_contents(path):
    with open(path, "r") as f:
        return f.read()


def split_log_into_blocks(log_contents):
    blocks = {}
    if log_contents:
        for line in log_contents.splitlines():
            try:
                date = datetime.datetime.strptime(line.split()[0], "%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue
            blocks[date] = line + "\n"
    return blocks


def search_by_date(blocks, date):
    if date is None:
        return blocks
    elif date == "":
        return {}
    else:
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
        return {
            date: block
            for date, block in blocks.items()
            if date_obj == date or date_obj > date or date_obj < date
        }


def search_by_text(blocks, text):
    if text is None:
        return blocks
    elif text == "":
        return {}
    else:
        return {
            date: block
            for date, block in blocks.items()
            if text in block
        }


def print_results(blocks, limit):
    if not blocks:
        print("No logs found.")
        return

    limit = int(limit)
    for date, block in blocks.items():
        print(f"Дата: {date}")
        print(block[:limit])


def main():
    args = parse_args()

    if args.file is None:
        args.file = os.getcwd()

    if not os.path.isdir(args.file):
        logs = get_file_contents(args.file)
        blocks = split_log_into_blocks(logs)
    else:
        blocks = {}
        for path in os.listdir(args.file):
            if path.endswith(".log"):
                log_contents = get_file_contents(os.path.join(args.file, path))
                blocks = merge_dicts(blocks, split_log_into_blocks(log_contents))

    blocks = search_by_date(blocks, args.date)
    blocks = search_by_text(blocks, args.text)

    print_results(blocks, args.limit)


if __name__ == "__main__":
    main()
