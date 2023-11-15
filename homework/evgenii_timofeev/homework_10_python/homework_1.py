def calc_decorator(func):
    def wrapper(number_1, number_2, operator):
        if number_1 == number_2:
            operator = "+"
        elif number_1 < 0 or number_2 < 0:
            operator = "*"
        elif number_1 > number_2:
            operator = "-"
        elif number_2 > number_1:
            operator = "/"

        return func(number_1, number_2, operator)

    return wrapper


@calc_decorator
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second
    else:
        return first * second


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

print(calc(first_number, second_number, "*"))
