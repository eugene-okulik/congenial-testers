from random import randint


def guess_number(random_numb):
    while True:
        user_numb = int(input('Попробуй угадать загаданное число! Введи его сюда: '))
        if random_numb == user_numb:
            print('Поздравляю! Вы угадали!')
            break
        else:
            print('Попробуйте снова')


random_numb_generator = randint(1, 10)
guess_number(random_numb_generator)
