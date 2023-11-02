
# task 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

text1 = f'person{'name, last_name, city, phone, country'}'
print(text1)

# task 2

text_one_42 = "результат операции: 42"
text_two_54 = "результат операции: 54"

srez1 = int(text_one_42[text_one_42.index('42'):])
srez2 = int(text_two_54[text_two_54.index('54'):])

print(srez1 + 10)
print(srez2 + 10)

# task 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
