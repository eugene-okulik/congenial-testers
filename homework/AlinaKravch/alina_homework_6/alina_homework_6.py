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
