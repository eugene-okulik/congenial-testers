def fibonachy_generator():
    number_1, number_2 = 0, 1
    while True:
        yield number_1
        number_1, number_2 = number_2, number_1 + number_2


positions = [5, 200, 1000, 100000]
link_for_fibonachy_generator = fibonachy_generator()

for item, value in enumerate(link_for_fibonachy_generator):
    if item in positions:
        print(f"Позиция элемента {item} = {value}")
    elif item >= max(positions):
        break
