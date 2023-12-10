def is_hot(temp):
    return temp > 28


temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

hot_days = list(filter(is_hot, temperatures))

print("Самая высокая температура:", max(hot_days))
print("Самая низкая температура:", min(hot_days))
print("Средняя температура:", sum(hot_days) / len(hot_days))
