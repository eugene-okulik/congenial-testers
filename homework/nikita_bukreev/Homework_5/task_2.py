# возможно я не совсем понял данное задание((

string_1 = 'результат операции: 42'
string_2 = 'Результат ОПЕРАЦИИ: 53453454'

replace_str_1 = string_1.replace(' ', '')
index_str_1 = replace_str_1.index(':')
print(int(replace_str_1[index_str_1:].replace(':', '')) + 10)

replace_str_2 = string_2.replace(' ', '')
index_str_2 = replace_str_2.index(':')
print(int(replace_str_2[index_str_2:].replace(':', '')) + 10)
