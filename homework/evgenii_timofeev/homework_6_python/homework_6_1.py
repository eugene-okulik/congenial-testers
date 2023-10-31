text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)
text_for_changes = text.split()
list_for_print = []
changes = "ing"

for word in text_for_changes:
    if word[-1].isalpha():
        list_for_print.append(word + changes)
    else:
        list_for_print.append(word[:-1] + changes + word[-1])

print(" ".join(list_for_print))
