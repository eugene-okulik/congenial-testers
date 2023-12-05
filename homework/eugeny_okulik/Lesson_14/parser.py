with open('av.txt') as av_file:
    data = av_file.read()

sections = data.split('\n\n')
# print(sections)
# options = list(map(lambda x: x.replace('\n', ';:'), sections))
# print(options)

features = {}
for option in sections:
    # print(option)
    # categ_title, *values = option.split('\n')
    options_list = option.split('\n')  # ['Экстерьер', 'легкосплавные диски', 'рейлинги на крыше', 'фаркоп']
    categ_title = options_list[0]
    values = options_list[1:]
    # print(categ_title, values)
    # features[categ_title] = values
    # features.update({title: values for title, *values in option.split('\n')})

print(features)
# print(features['Подушки'])


# lines = data.splitlines()
# print(lines)
#
# features = {}
# new_category = True
# current_categ = None
# for line in lines:
#     if not line:
#         new_category = True
#         current_categ = None
#         continue
#     if new_category:
#         features[line] = []
#         current_categ = line
#         new_category = False
#     else:
#         features[current_categ].append(line)
#
# print(features['Подушки'])
