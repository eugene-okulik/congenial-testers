# Task №1
person = ["John", "Doe", "New York", "+1372829383739", "US"]
name, last_name, city, phone, country = person

# Task №2
data_one = "результат операции: 42"
data_two = "результат операции: 54"
print(
    f"Результат первой строки = {float(data_one[data_one.index("42"):]) + 10} \n"
    f"Результат второй строки = {float(data_two[data_two.index("54"):]) + 10} \n",
)

# Task №3
students = ["Ivanov", "Petrov", "Sidorov"]
subjects = ["math", "biology", "geography"]
print(f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}")
