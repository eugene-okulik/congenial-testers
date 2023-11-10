stored_numb = 7
while True:
    user_numb = int(input('Угадайте число. Введите число от 1 до 10: '))
    if user_numb == stored_numb:
        break
    else:
        print('Попробуйте снова')
print('Поздравляю! Вы угадали!')
