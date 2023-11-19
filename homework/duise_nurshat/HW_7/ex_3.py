text1 = "результат операции: 42"
text2 = "результат операции: 54"
text3 = "результат работы программы: 209"
text4 = "результат: 2"


def add_ten_to_numbers(text):
    srez = int(text[text.index(':') + 2:])
    new_numb = srez + 10
    print(new_numb)

add_ten_to_numbers(text1)
