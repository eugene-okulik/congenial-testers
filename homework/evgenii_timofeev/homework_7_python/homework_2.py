def dict_parser(dict_for_parsing: dict[str, int]) -> None:
    for key, value in dict_for_parsing.items():
        print(key * value)


words = {"I": 3, "love": 5, "Python": 1, "!": 50}

dict_parser(words)
