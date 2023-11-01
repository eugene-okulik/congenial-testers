person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

a = "результат операции: 42"
b = "результат операции: 54"

suma = a.index(a.split()[-1])
sumb = b.index(b.split()[-1])

print(
    f"Первый результат операции = {int(a[suma:]) + 10} \n"
    f"Второй результат операции = {int(b[sumb:]) + 10} \n"
)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}')
