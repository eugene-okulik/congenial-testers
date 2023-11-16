import statistics
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
                ]

warm_days = list(filter(lambda x: x > 28, temperatures))
print(f'В самые жаркие дни была следующая температура: \n{warm_days}')

# avg_temp = sum(warm_days) / len(warm_days)
print(f'Минимальная температура - {min(warm_days)}°C \n'
      f'Максимальная температура - {max(warm_days)}°C \n'
      f'Средняя температура - {(statistics.mean(warm_days)):.2f}°C'
      )
