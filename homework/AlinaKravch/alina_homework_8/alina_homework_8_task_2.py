def num_fib():
    num_1 = 0
    num_2 = 1
    while True:
        num_3 = num_1 + num_2
        num_1 = num_2
        num_2 = num_3
        numb_fibonacci = num_2 - num_1
        yield numb_fibonacci


def find_num_fib(*numb):
    count = 0
    for x in num_fib():
        count += 1
        if count in numb:
            print(x)
        if count >= max(numb):
            break


find_num_fib(5, 200, 1000)
find_num_fib(100000)
