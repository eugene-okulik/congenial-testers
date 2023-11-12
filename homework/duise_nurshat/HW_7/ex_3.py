text1 = "результат операции: 42"
text2 = "результат операции: 54"
text3 = "результат работы программы: 209"
text4 = "результат: 2"

def func(text, numb):
    srez = int(text[text.index(numb):])
    print(srez + 10)

func(text3, '209')
