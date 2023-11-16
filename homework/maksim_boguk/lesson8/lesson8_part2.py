def fibonacci():
    numb1 = 0
    numb2 = 1
    while True:
        yield numb1
        numb1, numb2 = numb2, numb1 + numb2


count = 1

range_to_compare = [4, 199, 999]
for numb in fibonacci():
    count += 1
    if count in range_to_compare:
        print(numb)
    if count > 999:
        break
