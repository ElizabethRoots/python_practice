
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dict2 = {'c': 10, 'd': 20, 'e': 30, 'f': 40, 'g': 50}

# Expression computes shared keys using set intersection
dict1_a = set(dict1)
dict2_b = set(dict2)

shared_keys = dict1_a.intersection(dict2_b)
print(len(shared_keys))

# Expressiong computes shared values
shared_values = dict1.items() & dict2.items()
print(len(shared_values))

# Extra solutions
print("Extra solutions: ")

# Expression computes shared keys
shared_key = dict1.keys() & dict2.keys()
print(len(shared_key))

# For loop appends shared keys
shared_value = []
for item in dict1_a.intersection(dict2_b):
    shared_value.append(item)
print(shared_value)
print(len(shared_value))

# Expression computes shared key using set intersection
shared_val = set(dict1.keys()).intersection(dict2.keys())
print(shared_val)
print(len(shared_val))
