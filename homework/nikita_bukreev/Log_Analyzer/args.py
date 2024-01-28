from functions import parse_args, read_file, date_parser, find_date, filter_by_date, find_text
# from functions import print_colored_dict


def work_pls():
    file_path, date, text, unwanted, full = parse_args()
    data = read_file(file_path)
    if date is not None and text is not None:
        flag, *user_date = date_parser(date)
        list_of_dates = find_date(data.keys(), flag, *user_date)
        result = filter_by_date(data, list_of_dates)
        result = find_text(result, text, unwanted, full)
    elif date is None and text is not None:
        result = find_text(data, text, unwanted, full)
    elif date is not None and text is None:
        flag, *user_date = date_parser(date)
        list_of_dates = find_date(data.keys(), flag, *user_date)
        result = filter_by_date(data, list_of_dates)
    elif date is None and text is None and unwanted is not None:
        result = find_text(data, text, unwanted, full)
    else:
        result = data
    return result
    # return print_colored_dict(result, text)
    # не смог подебажить колораму, т.к. в терминале мака (в том числе и в пайчарме) вместо цвета я вижу код цветов,
    # который тяело разглядеть в логах(( если получится зпустить код на убунту - то можно раскоментить строчку с
    # с ретерном и импортом=)


print(work_pls())
