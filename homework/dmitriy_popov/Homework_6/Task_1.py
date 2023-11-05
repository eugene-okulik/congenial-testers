text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. \n'
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = text.split()
fin_words = []
for word in words:
        if word.endswith((',', '.')):
                word = word.replace(word[-1], 'ing') + word[-1]
        else:
                word = word + 'ing'
        fin_words.append(word)
print(' '.join(fin_words))










