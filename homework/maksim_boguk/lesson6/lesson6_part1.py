word = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel.'
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

new_word = word.split()
changes_word = []
chang = "ing"

for word in new_word:
    if word[-1].isalpha():
        changes_word.append(word + chang)
    else:
        changes_word.append(word[:-1] + chang + word[-1])

print(' '.join(changes_word))
