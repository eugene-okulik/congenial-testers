# Пример строк с результатами операции
result1 = "operation result: 42"
result2 = "operation result: 54"

# Извлечение чисел, прибавление 10 и печать результатов
print("Result 1:", int(result1.split()[-1]) + 10)
print("Result 2:", int(result2.split()[-1]) + 10)
