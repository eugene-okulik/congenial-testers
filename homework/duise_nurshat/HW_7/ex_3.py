import re

def add_ten_to_numbers(text):
    numbers = re.findall(r'\d+', text)
    modified_numbers = [int(number) + 10 for number in numbers]
    return modified_numbers


text1 = int(input('результат операции: '))
text2 = int(input('результат операции: '))
text3 = int(input('результат работы программы: '))
text4 = int(input('результат: '))

# Получаем числа из каждой строки и добавляем к ним 10
numbers_text1 = add_ten_to_numbers(text1)
numbers_text2 = add_ten_to_numbers(text2)
numbers_text3 = add_ten_to_numbers(text3)

# Вывод измененных чисел
print("Числа из первой строки + 10:", numbers_text1)
print("Числа из второй строки + 10:", numbers_text2)
print("Числа из третьей строки + 10:", numbers_text3)
