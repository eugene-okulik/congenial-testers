res_1 = 'результат выполнения операции: 42'
res_2 = 'результат операции: 54'
res_3 = 'результат работы программы: 209'
res_4 = 'результат: 2'


def calc(numb):
    colon = numb.index(':')
    result = int(numb[colon + 2:]) + 10
    print(f'Результат сложения: {result}')


calc(res_1)
calc(res_2)
calc(res_3)
calc(res_4)
