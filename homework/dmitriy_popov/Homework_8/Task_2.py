def fibonacci():
    num_1 = 0
    num_2 = 1
    while True:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


def numb_fibonacci(*numb):
    count = 0
    for x in fibonacci():
        count += 1
        if count in numb:
            print(x)
        if count >= max(numb):
            break


numb_fibonacci(5, 200, 1000, 100000)
