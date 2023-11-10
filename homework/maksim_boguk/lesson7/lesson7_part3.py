a = 'результат операции: 42'
b = 'результат операции: 54'
c = 'результат работы программы: 209'
d = 'результат: 2'


def calc(results):
    res = results.index(':')
    result = int(results[res + 2:]) + 10
    print(f'Итого: {result}')


calc(a)
calc(b)
calc(c)
calc(d)
