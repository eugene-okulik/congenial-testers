temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24,
    23
]

hot = list(filter(lambda temp: temp > 28, temperatures))
print('Список жарких дней: ', hot)
print('Cамая высокая температура ', max(hot))
print('Cамая низкая температура ', min(hot))
print('Средняя температура: ', sum(hot) / len(hot))
