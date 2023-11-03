import random


def counter(*args) -> None:
    for sentence in args:
        number_index = sentence.index(sentence.split()[-1])
        print(
            f"Результат операции после сложения = {float(sentence[number_index:]) + 10}"
        )


data_one = "результат операции: 42"
data_two = "результат операции: 54"

counter(data_one, data_two, "результат операции: " + str(random.randint(1, 1001)))
