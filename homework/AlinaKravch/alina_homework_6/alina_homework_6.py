# + ‘ing’ ending to each word in the text
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,
# facilisis vitae semper at, dignissim vitae libero” and afterward the final text should be printed.

my_text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
           'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
added_ending = 'ing'
text_list = my_text.split()
new_text_list = []
for word in text_list:
    if word.endswith(','):
        new_word = word.replace(',', '')
        new_word += added_ending + ','
        new_text_list.append(new_word)
    elif word.endswith('.'):
        new_word = word.replace('.', '')
        new_word += added_ending + '.'
        new_text_list.append(new_word)
    else:
        word += added_ending
        new_text_list.append(word)
print(' '.join(new_text_list))

# Write a program that tries the sequence from 1 to 100. For numbers divisible by 3 it should write:
# "Fuzz" instead of printing the number, and for numbers divisible by 5 it should print "Buzz".
# For numbers that are multiples of both 3 and 5, it should print "FuzzBuzz". Otherwise, print the number.

for n in range(1, 101):
    if n % 3 == 0:
        print('Fuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif (n % 3 == 0) and (n % 5 == 0):
        print('FuzzBuzz')
    else:
        print(n)
