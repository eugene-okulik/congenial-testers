import statistics
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
                ]
# норм ли сразу так записать list(fiter ....)?
# как альтернативу вижу в f-строку впихнуть

warm_days = (filter(lambda x: x > 28, temperatures))
print(f'В самые жаркие дни была следующая температура: \n{(list(warm_days))} ')

# avg_temp = sum(temperatures) / len(temperatures)
#  хз норм ли все в f-строку, но раз нам не надо использовать это дальше, не создавал переменные
print(f'Минимальная температура - {min(temperatures)}°C \n'
      f'Максимальная температура - {max(temperatures)}°C \n'
      f'Средняя температура - {int(statistics.mean(temperatures))}°C'
      )
