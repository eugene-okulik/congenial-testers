mystic_num = 7
while True:
    user_input = int(input('Enter mystic number:'))
    if user_input == mystic_num:
        break
    else:
        print("Попробуйте снова")
        continue

print("Поздравляю! Вы угадали!")
