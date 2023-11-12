def fibonacci():
    num1 = 0
    num2 = 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


count = 1

range_to_compare = [5, 199, 999]
for num in fibonacci():
    count += 1
    if count in range_to_compare:
        print(num)
    if count > 999:
        break
