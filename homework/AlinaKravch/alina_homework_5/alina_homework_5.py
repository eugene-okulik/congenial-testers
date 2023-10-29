# Task 1
# Unpack 'person'
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(person)

# Task №2
# 52 and 64
text_1 = 'the result of operation_1: 42'
text_2 = 'the result of operation_2: 54'
text_1_index = text_1.index(text_1[-3:])
text_2_index = text_2.index(text_2[-3:])

print(
    f'the result of operation_1 : {int(text_1[text_1_index:]) + 10} \n'
    f'the result of operation_2 : {int(text_2[text_2_index:]) + 10} \n',
)

# Task №3
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geograpy
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['Math', 'Biology', 'Geography']

print(f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}.")

