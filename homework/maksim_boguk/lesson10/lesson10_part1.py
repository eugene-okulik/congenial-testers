def decoration(decor):
    def wrapper(first, second, operation):
        if first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        elif first < 0 or second < 0:
            operation = "*"
        elif first < second:
            operation = "/"

        return decor(first, second, operation)

    return wrapper


@decoration
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second
    else:
        return first * second


first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))

print(calc(first, second, "*"))
