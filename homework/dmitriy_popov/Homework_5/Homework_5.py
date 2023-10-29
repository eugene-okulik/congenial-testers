# Task 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person


# Task 2
result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'

number_1 = int(result_1[-2:])
sum_1 = number_1 + 10
print(f'Результат сложения: {sum_1}')

number_2 = int(result_2[-2:])
sum_2 = number_2 + 10
print(f'Результат сложения: {sum_2}')


# Task 3 Variant 1
students = ['Ivanov', 'Petrov', 'Sidorov']
st_1, st_2, st_3 = students
subjects = ['math', 'biology', 'geography']
sub_1, sub_2, sub_3 = subjects
print(f'Students {st_1}, {st_2}, {st_3} study these subjects: {sub_1}, {sub_2}, {sub_3}')

# Task 3 Variant 2
students_1 = ['Ivanov', 'Petrov', 'Sidorov']
subjects_2 = ['math', 'biology', 'geography']
print(f'Students {", ".join(students_1)} study these subjects: {", ".join(subjects_2)}')
