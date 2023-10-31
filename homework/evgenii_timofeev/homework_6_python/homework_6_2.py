text_1 = "Fuzz"
text_2 = "Buzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(text_1 + text_2)
    elif number % 5 == 0:
        print(text_2)
    elif number % 3 == 0:
        print(text_1)
    else:
        print(number)
