znachenie = 7
while True:
    user_input = int(input('Введите ЦИФРУ: '))
    if user_input == znachenie:
        break
    else:
        print('попробуйте снова')
print('Поздравляю! Вы угадали!')
