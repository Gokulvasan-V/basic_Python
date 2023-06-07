#Dictionary Keys

dict_1 = {
    123 : 'hello',
    True : 1223,

}

print(dict_1[123])
print(dict_1[True])
print(dict_1.items()) # it will show the (keys, values) in tuple format.

"""
dictionary key always has to be immutable.
"""
#print(dict['age']) # it will show error, because we did't mention 'age' in our dict.

#Dictionary method 1

"""
.get is a method on the object or the dictionary in Python.
"""
print(dict_1.get('age')) # Now it will show 'None', because we added the 'age' key but didn't add value.
print(dict_1.get('age',456)) # (key, value)

"""
Another way to create a dictionary,
which is not very common way.
"""

dict_2 = dict (name='Gokulvasan')
print(dict_2)

#Dictionary method 2

print ('name' in dict_2)

print(dict_1.items()) # it will stores in tuple.

#clear
dict_3 = {'hello' : '3891'}
dict_3.clear() # delete all elements.
print(dict_3)

#copy
dict_2_1 = dict_2.copy()
print(dict_2)
print(dict_2_1)

#pop
dict_1_1 = dict_1.copy()
print(dict_1_1)
print(dict_1_1.pop(True)) # we want to mention the which key we want to remove.

dict_4 = {1: 'Geeks', 2: 'For',
        3:'hello' ,'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}
  
print(dict_4)

print(dict_4.pop('A')) # We can mention specifically by key.

print(dict_4)

print(dict_4.popitem()) # It randomly pops up something.

print(dict_4)

# update

dict_4.update({3:'hii'})
print(dict_4)

"""
Want to know more
Dictionary Methods --> https://www.w3schools.com/python/python_ref_dictionary.asp
"""