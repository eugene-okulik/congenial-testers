# Using slices and the index method, get a number from each line with the result,
# add 10 to the resulting number, print the result of the addition. The functions
# should be used.
import random


# def counter(*args) -> None:
#     for sentence in args:
#         number_index = sentence.index(sentence.split()[-1])
#         print(
#             f"Результат операции после сложения = {float(sentence[number_index:]) + 10}"
#         )


# data_one = "результат операции: 42"
# data_two = "результат операции: 54"

# counter(data_one, data_two, "результат операции: " + str(random.randint(1, 1001)))







res_1 = 'результат выполнения операции: 42'
res_2 = 'результат операции: 54'
res_3 = 'результат работы программы: 209'
res_4 = 'результат: 2'


def calc(numb):
    colon = numb.index(':')
    result = int(numb[colon + 2:]) + 10
    print(f'Результат сложения: {result}')


calc(res_1)
calc(res_2)
calc(res_3)
calc(res_4)












def calc(stroka):
    results = stroka.split(' ')[-1]
    results = int(results) + 10
    print(f'Результат сложения: {results}')


stroka = ['результат операции: 42',
          'результат операции: 54',
          'результат работы программы: 209',
          'результат: 2'
          ]

for results in stroka:
    calc(results)








def find_result_operatoin(*result_strings):
    for i in result_strings:
        split_string = i.split()
        last_element = split_string[-1]
        if last_element.isdigit() is False:
            print(f'Результат операции вернул следующее нецифровое занчение: {last_element}')
        else:
            print(int(last_element) + 10)


example_1 = 'результат операции: 42'
example_2 = 'результат операции: 54'
example_3 = 'результат работы программы: 209'
example_4 = 'результат: 2'
example_5 = 'результат: ОШИБКА'  # решил попробовать сделать проверку являтся ли результат числом

find_result_operatoin(example_1, example_2, example_3, example_4, example_5)