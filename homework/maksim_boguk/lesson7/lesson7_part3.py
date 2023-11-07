a = 'результат операции: 42'
b = 'результат операции: 54'
c = 'результат работы программы: 209'
d = 'результат: 2'


def calc(numb):
    search = numb.index(':')
    res1 = int(numb[search + 2:]) + 10
    print(f'Итого: {res1}')


calc(a)
calc(b)
calc(c)
calc(d)
