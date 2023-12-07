def fibonacci_num():
    a = 0
    b = 1
    count = 0
    while True:
        yield a
        a = b
        b = a + b
        count += 1


def fib_sequence(*desired_length):
    count = 0
    for x in fibonacci_num():
        count += 1
        if count in desired_length:
            print(x)
        if count >= max(desired_length):
            break


fib_sequence(5, 200, 1000)
