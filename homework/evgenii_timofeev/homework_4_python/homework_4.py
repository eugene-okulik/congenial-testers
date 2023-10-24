my_dict = {
    "tuple": (1, 2, 3, 4, 5),
    "list": [6, 7, 8, 9, 0],
    "dict": {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5},
    "set": {1, 2, 3, 4, 5},
}

# Show last element
print(my_dict["tuple"][-1])

# Add one element to a list and delete one element from the list
my_dict["list"].append(1)
my_dict["list"].pop(1)

# Add one element to a tuple and delete one element from the tuple
my_dict["dict"]["i am a tuple"] = "it's a lie. I'm not a tuple"
del my_dict["dict"]["one"]

# Add one element to set and delete one element from the set
my_dict["set"].add(6)
my_dict["set"].discard(1)

# Print the final dictionary
print(my_dict)
