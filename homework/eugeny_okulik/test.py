result = [{'12.01.2023': 'Error message'}, {'12.01.2023': 'Warning message'}]
result = {
    '12.01.2023 13:00': '12.01.2023 13:00 Error message',
    '12.01.2023 13:01': '12.01.2023 13:01 Warning message',
    '12.01.2023 13:02': '12.01.2023 13:02 Error message appeared'
}

text = 'Error'
unwanted = 'appeared'

# for x in result:
#     print(x.values())

# result = list(filter(lambda x: text in list(x.values())[0], result))
result = list(filter(lambda x: text in x[1], result.items()))
result = dict(result)
result = list(result.values())

result = list(filter(lambda x: unwanted not in x, result))

for res in result:
    print(res)
    print(res.index(text))
    print(res[res.index(text):res.index(text) + 10])

# print(result)
