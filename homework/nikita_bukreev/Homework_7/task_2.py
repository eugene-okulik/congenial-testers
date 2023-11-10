
def refactor_dict(words):
    for word, count in words.items():
        print(word * count)


task_words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
refactor_dict(task_words)
