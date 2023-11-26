# Using slices and the index method, get a number from each line with the result,
# add 10 to the resulting number, print the result of the addition. The functions.py
# should be used.
def calc(string):
    result = string.split()[-1]
    result = int(result) + 10
    print(f'The result of calculation: {result}')


string = ['res_1: 42',
          'res_2: 54',
          'res_3: 209',
          'res_4: 2'
          ]

for result in string:
    calc(result)
