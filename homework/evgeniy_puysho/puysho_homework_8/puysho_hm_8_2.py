def fibonacci():
    num_1 = 0
    num_2 = 1
    while True:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


count = 0

# хм, не уверен, но раз нужно вывести число n, то в ренже надо указать n-1, тк счет с нуля, да?
range_to_compare = [4, 199, 999]
for num in fibonacci():
    count += 1
    if count in range_to_compare:
        print(num)
    if count > 999:
        break
