text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')

rep = text.replace(',', '').replace('.', '')
words = rep.split()
new_text = []
for word in words:
    new_text.append(word + 'ing')

result = " ".join(new_text)
print(result)
