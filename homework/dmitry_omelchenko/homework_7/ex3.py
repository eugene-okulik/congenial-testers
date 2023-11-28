def process_result(line):
    number = int(line.split(':')[-1]) + 10
    print(number)


lines = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for line in lines:
    process_result(line)

