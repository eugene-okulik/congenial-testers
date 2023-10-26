dictionary = {'my_tuple':(1, 2.5, 'Alina', 4, True), 
            'my_list': [1,  False, 2.42, 'last', 'last2'], 
            'my_dict': {'one': True, 'two': 'Friend', 'three': 3, 'four': 2.6, 'five': False},  
            'my_set':{3, None, 'Fine', False, 2.42}} 

print(dictionary['my_tuple'][-1]) 
dictionary['my_list'].append(43) 
dictionary['my_list'].pop(2) 
dictionary['my_dict']['i am a tuple'] = 'Alex' 
del dictionary['my_dict']['two'] 
dictionary['my_set'].add('end') 
dictionary['my_set'].remove('end') 
print(dictionary) 