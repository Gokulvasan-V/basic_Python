"""
Tuple are like lists, but unlike lists we cannot modify them.
There are immutable
"""

a = 1,2,3,4,5,6
print(type(a)) # Tuple is the default type.

my_tup = (1,2,3,4,5,6)
print(my_tup)
print(my_tup[1]) # can access it through an index.

print(5 in my_tup)

#my_tup[1] = 'tup' # we can't modify.

"""
Once you create it, we can't modify.
You can't sort it or reverse it
"""

user = {
    (1,2) : [1,2,3,4,5],
    'greet' : 'hello',
    'age' : 23
} # we can give key in tuple format.

print(user)
print(user[(1,2)])
