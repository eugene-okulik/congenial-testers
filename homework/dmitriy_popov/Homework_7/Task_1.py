number = 7
print('Давай поиграем в "Угадай цифру"')
while True:
    user_input = int(input('Введите число от 1 до 10: '))
    if user_input == number:
        break
    else:
        print('Попробуйте снова')

print('Поздравляю! Вы угадали!')
