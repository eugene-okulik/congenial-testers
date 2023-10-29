#Дан такой список:
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
#С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:
#name, last_name, city, phone, country

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name = 'John'
last_name = 'Doe'
city = 'New York'
phone = '+1372829383739'
country = 'US'

#Допустим, какая-то программа возвращает результат своей работы в таком виде:
#результат операции: 42
a = ['результат', 'операции:', 42]
a1 = 42
sum1 = a1 + 10
print(sum1)

#Допустим, какая-то программа возвращает результат своей работы в таком виде:
#результат операции: 54
b = ['результат', 'операции:', 54]
b1 = 54
sum2 = b1 + 10
print(sum2)


#Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен
#выглядеть так:
#Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geograpy
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print('Students Ivanov, Petrov, Sidorov study these subjects:', ',' ' ' .join(subjects))