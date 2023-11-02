my_text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '\
          'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
words = my_text.split()
new_text = []
for word in words:
    '''
    вот так вот я изначально сделал, но потом переписал
    if word.endswith('.'):
    word = word.replace('.', 'ing') + '.'
    if word.endswith(','):
    word = word.replace('.', 'ing') + ','
    '''
    if word.endswith((',', '.')):
        word = word.replace(word[-1], 'ing') + word[-1]
    else:
        word = word + 'ing'
    new_text.append(word)
print(' '.join(new_text))
