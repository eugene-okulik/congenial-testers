number = 7
print('Давай поиграем в "Угадай цифру"')
while True:
    user_input = int(input('Введите число от 1 до 10: '))
    if user_input == number:
        break
    elif user_input != number:
        print('Попробуйте снова')
        continue

print('Поздравляю! Вы угадали!')
