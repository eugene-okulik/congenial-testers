text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')

words = text.split()

new_text = []
for word in words:
    if word.endswith((',', '.')):
        word = word.replace(word[-1], 'ing') + word[-1]
    else:
        word = word + 'ing'
    new_text.append(word)

result = " ".join(new_text)
print(result)
