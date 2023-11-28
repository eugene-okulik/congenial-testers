number = 7

while True:
    input_number = int(input("Введите цифру: "))

    if input_number == number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова.")

