import random


def fibonachy_generator(position):
    # we need add 1 because we start counting from 0
    position = position + 1
    number_1, number_2, checker = 0, 1, 0
    while checker != position:
        yield number_1
        number_1, number_2 = number_2, number_2 + number_1
        checker += 1


position_of_user = random.randint(0, 10000)
link_for_fibonachy_generator = fibonachy_generator(position_of_user)

for item, value in enumerate(link_for_fibonachy_generator):
    if item != position_of_user:
        continue
    else:
        print(f"Позиция элемента {item} = {value}")
