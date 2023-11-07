def fibonacci():
    num_1 = 0
    num_2 = 1
    while True:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


count = 0
for num in fibonacci():
    count += 1
    if count == 5:
        print(num)
    elif count == 200:
        print(num)
    elif count == 1000:
        print(num)
        break
