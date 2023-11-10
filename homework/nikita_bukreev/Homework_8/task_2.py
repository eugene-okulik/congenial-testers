# Захотелось в конце немного поиграться с try и except =)

def fibonacci():
    f1 = 0
    f2 = 1
    while True:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        numb_fibonacci = f2 - f1
        yield numb_fibonacci


def find_numb_fibonacci(*numb):
    count = 0
    for x in fibonacci():
        count += 1
        if count in numb:
            print(x)
        if count >= max(numb):
            break


try:
    find_numb_fibonacci(5, 200, 1000)
    print('Посчитано число Фибоначи для 5, 200 и 1000 элемента!')
    print('Рассчитываю число для 100000 элемента')
    find_numb_fibonacci(100000)
    print('Посчитано число для 100000 элемента')
except ValueError as v:
    print(f'Упс, для 100000 элемента не получилось сделать вычисления, появилась следующая ошибка {v}')
