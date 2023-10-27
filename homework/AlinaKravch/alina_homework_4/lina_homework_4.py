dictionary = {
    'my_tuple': (1, 2.5, 'Alina', 4, True),
    'my_list': [1, False, 2.42, 'last', 'last2'],
    'my_dict': {'one': True, 'two': 'Friend', 'three': 3, 'four': 2.6, 'five': False},
    'my_set': {3, None, 'Fine', False, 2.42}
}

# Print the last element
print(dictionary['my_tuple'][-1])

# Add one more element and delete the second one from the list
dictionary['my_list'].append(43)
dictionary['my_list'].pop(2)

# Add one more element with the key 'I am a tuple' and delete any element
dictionary['my_dict']['i am a tuple'] = 'Alex'
del dictionary['my_dict']['two']

# Add one element to the set and delete one element from the set
dictionary['my_set'].add('end')
dictionary['my_set'].remove('end')

# Print the changed dictionary
print(dictionary)
