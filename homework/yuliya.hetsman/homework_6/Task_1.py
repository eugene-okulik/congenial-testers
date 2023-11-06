text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. \
        Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

some_text = text.split()
new_text = []
chars = 'ing'

for word in some_text:
    if word.endswith((',', '.')):
        word = word.replace(word[-1], 'ing') + word[-1]
    else:
        word = word + 'ing'
    new_text.append(word)
print(' '.join(new_text))
