# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,
# facilisis vitae semper at, dignissim vitae libero” и после этого выводит получившийся текст на экран.

text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
add_end = 'ing'
text_list = text.split()
new_text_list = []
for word in text_list:
    if word.endswith(','):
        new_word = word.replace(',', '')
        new_word += add_end + ','
        new_text_list.append(new_word)
    elif word.endswith('.'):
        new_word = word.replace('.', '')
        new_word += add_end + '.'
        new_text_list.append(new_word)
    else:
        word += add_end
        new_text_list.append(word)
print(' '.join(new_text_list))
