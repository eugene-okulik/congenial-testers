import statistics


temps = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]


warm_temps = list(filter(lambda x: x > 28, temps))
print(f'List of hot days: {warm_temps}')
print(f'The highest temperature: {max(warm_temps)}')
print(f'The lowest temperature: {min(warm_temps)}')
print(f'Average temperature: {int(statistics.mean(warm_temps))}')
