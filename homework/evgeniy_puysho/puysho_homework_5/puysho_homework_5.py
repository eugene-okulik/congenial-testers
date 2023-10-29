# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# Задание 2
res_1 = 'результат операции: 42'
res_2 = 'результат операции: 54'

# я может чего не уловил, но не понял, для чего index, если тут достаточно среза
num_1 = int(res_1[-2:])
num_2 = int(res_2[-2:])

# если бы нужно было использовать дальше, то загнал бы в переменные, но для задания вроде так тоже ок
# num_1 += 10
# num_2 += 10
print(num_1 + 10, num_2 + 10, sep='\n')

# Задание 3
# Я попробовал все, начиная от загона через переменные st1, st2 и тд, и дошел до этого по итогу:
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print(f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}')
