# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# Задание  2
res_1 = 'результат операции: 42'
res_2 = 'результат операции: 54'
num_1 = res_1.index(': ') + 2
num_1 = int(res_1[num_1:])

# сделал в одну строку ради интереса, но будто бы читается не супер
num_2 = int(res_2[res_2.index(': ') + 2:])
print(num_1 + 10, num_2 + 10, sep='\n')

# Задание 3
# Я попробовал все, начиная от загона через переменные st1, st2 и тд, и дошел до этого по итогу
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print(f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}')
