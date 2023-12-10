text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, "
        "dignissim vitae libero")

words = text.split()
modified_words = []  # Создание списка для модифицированных слов
for word in words:
    # Проверяем, если в слове есть запятая или точка в конце, то добавляем 'ing' перед
    if word.endswith('.'):
        modified_word = word[:-1] + 'ing.'
    elif word.endswith(','):
        modified_word = word[:-1] + 'ing,'
    else:
        modified_word = word + 'ing'  # Добавляем 'ing' к слову

    modified_words.append(modified_word)  # Добавление в список
modified_text = ' '.join(modified_words)  # Объединение в текст

print(modified_text)
