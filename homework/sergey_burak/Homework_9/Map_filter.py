# Есть такой список:
# temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
#                 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
# С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
# Будем считать жарким всё, что выше 28.
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
hotdays = []
days = 1
for t in temperatures:
    if t > 28:
        hotdays.append(days)
    days += 1
print(f"Жаркие дни: {hotdays}")

print(f'Температура в жаркие дни: {list(filter(lambda t: t > 28, temperatures))}\n'
      f'Максимальная температура: {max(filter(lambda t: t > 28, temperatures))}\n'
      f'Минимальная температура: {min(filter(lambda t: t > 28, temperatures))}\n'
      f'Средняя температура: '
      f'{round(sum(filter(lambda t: t > 28, temperatures)) / len(list(filter(lambda t: t > 28, temperatures))), 1)}')
