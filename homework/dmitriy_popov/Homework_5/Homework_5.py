# Task 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person


# Task 2
res_1 = 'результат выполнения операции: 42'
res_2 = 'результат операции: 54'

res_1_index = res_1.index(':') + 2
res_2_index = res_2.index(':') + 2

print(
    f'Результат первого сложения: {int(res_1[res_1_index:]) + 10} \n'
    f'Результат первого сложения: {int(res_2[res_2_index:]) + 10} \n'
)


# Task 3
students_1 = ['Ivanov', 'Petrov', 'Sidorov']
subjects_2 = ['math', 'biology', 'geography']
print(f'Students {", ".join(students_1)} study these subjects: {", ".join(subjects_2)}')
