
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
