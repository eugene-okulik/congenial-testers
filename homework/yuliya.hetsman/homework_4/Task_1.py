my_dict = {
    tuple: (1, 2, 3, 4, 5),
    list: [1, 'text', 0.5, False, 5],
    dict: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    set: {1, True, 2.5, 'word', 8}
}

# Last element for tuple:
print(my_dict[tuple][-1])

# Added an element to the end of the list:
my_dict[list].append(13)
# Deleted second element from list
my_dict[list].pop(1)

# Added element with key and value
my_dict[dict]['i am a tuple'] = 6
# Deleted some element from dict
my_dict[dict].pop('a')

# Added new element to set
my_dict[set].add(255)
# Deleted element from set
my_dict[set].remove(2.5)

print(my_dict)
