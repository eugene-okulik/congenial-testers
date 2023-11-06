def calc(stroka):
    results = stroka.split(' ')[-1]
    res = int(results) + 10
    print(f'Результат сложения: {results}')


stroka = ['результат операции: 42',
           'результат операции: 54',
           'результат работы программы: 209',
           'результат: 2'
           ]

for results in stroka:
    calc(results)
