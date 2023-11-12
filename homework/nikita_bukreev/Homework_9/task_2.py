
temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29,
    31, 33, 31, 30, 32, 30, 28, 24, 23
]
hot_temperature_f = list(filter(lambda temp: temp > 28, temperatures))
print('Список самых высоких температиур самых жарких дней: ', hot_temperature_f)
print('Самая высокая температура: ', max(hot_temperature_f))
print('Самая низкая температура: ', min(hot_temperature_f))
print('Средняя температура самых жарких дней: ', round(sum(hot_temperature_f) / len(hot_temperature_f), 2))


# попытался отфильтровать список ТОЛЬКО с помщью map, но получилось криво(
hot_temperature_m = map(lambda temp: temp if temp > 28 else None, temperatures)
new_list_hot_temp = list(hot_temperature_m)
while None in new_list_hot_temp:
    new_list_hot_temp.remove(None)
print(new_list_hot_temp)

new_list_hot_temp_2 = [temp for temp in new_list_hot_temp if temp != 5]
print(new_list_hot_temp_2)
