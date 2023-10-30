# Task №1
person = ["John", "Doe", "New York", "+1372829383739", "US"]
name, last_name, city, phone, country = person

# Task №2
data_one = "результат операции: 42"
data_two = "результат операции: 54"

data_one_index = data_one.index(data_one.split()[-1])
data_two_index = data_two.index(data_two.split()[-1])

print(
    f"Результат первой строки = {float(data_one[data_one_index:]) + 10} \n"
    f"Результат второй строки = {float(data_two[data_two_index:]) + 10} \n",
)

# Task №3
students = ["Ivanov", "Petrov", "Sidorov"]
subjects = ["math", "biology", "geography"]
print(f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}")
