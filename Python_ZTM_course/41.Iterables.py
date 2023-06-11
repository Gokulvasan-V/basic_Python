
# Iterables --> list,tuple, dict, set, string.
# Iterate --> one by one check each items in the collections.


user = {
    'name' : 'Gokul',
    'age' : 24,
    'can_swim' : False
}

for swim in user:
    print(swim) # if you run this, it will print only keys.
print('\n')

"""
dictionaries have three methods that are really, 
really useful when we want to loop over their keys and values.
"""

for swim in user.items():
    print(swim) # it will print keys & values pair in the tuple format.
print('\n')

for swim in user.values():
    print(swim) # it will print only the values of dict.
print('\n')

for swim in user.keys():
    print(swim) # it will print only the keys of dict.
print('\n')


"""
there's actually a shorthand way of being able to do this in here in the for loop.
"""

# can separate them into key and values.

for swim in user.items():
    keys, values = swim
    print(keys, values)
print('\n')

for key, values in user.items(): # key, values --> in the place we can give any name in this place.
    print(key, values) 

for items in 50:
    print(items) # it will show error because 'int' is not Iterables.