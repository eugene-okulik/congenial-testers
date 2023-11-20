# скажу честно, так и не понял, как это работает, великий gpt помог немного
# есть кейс, когда у тебя может быть два отрицательных числа, которые равны
def decorator(func):
    def inner(first_num, second_num, operation):
        if first_num < 0 or second_num < 0:
            operation = '*'
        elif first_num == second_num:
            operation = '+'
        elif first_num > second_num:
            operation = '-'
        elif first_num < second_num:
            operation = '/'
        return func(first_num, second_num, operation)
    return inner


@decorator
def calc(first_num, second_num, operation):
    if operation == '+':
        return first_num + second_num
    elif operation == '-':
        return first_num - second_num
    elif operation == '/':
        return first_num / second_num
    elif operation == '*':
        return first_num * second_num


first = float(input('Введи первое число: '))
second = float(input('Введи второе число: '))
print(calc(first, second, '/'))
