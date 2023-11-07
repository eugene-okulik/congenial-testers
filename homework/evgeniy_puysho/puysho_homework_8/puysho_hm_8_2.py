def fibonacci():
    num_1 = 0
    num_2 = 1
    while True:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


count = 0
range_to_compare = [3, 200, 1000]
for num in fibonacci():
    count += 1
    if count in range_to_compare:
        print(num)
    if count > 1000:
        break
