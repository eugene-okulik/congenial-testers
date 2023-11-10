# Задание №1
# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,
# facilisis vitae semper at, dignissim vitae libero”
# и после этого выводит получившийся текст на экран.

text1 = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, '
         'facilisis vitae semper at, dignissim vitae libero')
print(f"Исходный текст: {text1}")
result_text = []
for word in text1.split():
    if word.endswith(','):
        result_text.append(word[:-1] + 'ing,')
    elif word.endswith('.'):
        result_text.append(word[:-1] + 'ing.')
    else:
        result_text.append(word + 'ing')

print(f"Получившийся текст: {' '.join(result_text)}")
