def calc(func):
    def wrapper(num_1, num_2):
        if num_1 == num_2:
            operator = "+"
        elif num_1 > num_2:
            operator = "-"
        elif num_1 < 0 or num_2 < 0:
            operator = "*"
        elif num_2 > num_1:
            operator = "/"

        return func(num_1, num_2, operator)

    return wrapper


@calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second: "))

print(calc(numberOne, numberTwo))

