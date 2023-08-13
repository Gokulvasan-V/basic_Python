"""
map() function returns a map object(which is an iterator) 
of the results after applying the given function to each item of a given iterable (list, tuple etc.)

Syntax :
map(function, itereables)
"""

"""
we iterate the iterables(list, tuple, set and etc...) without using looping, instead of we are using map.
"""

# normal method
def addiction(n):
    return n+n

numbers = [1,2,3,4,5]
Lst = []

for i in numbers:
    Lst.append(addiction(i))

print(Lst) 

print("\nUsing map:")
#-------------------#-------------------#-------------------#-------------------#

Result = map(addiction, numbers)
print(list(Result))

#-------------------#-------------------#-------------------#-------------------#
print("\nUsing Lambda")

Result_2 = map(lambda x:x+x, numbers)
print(list(Result_2)) # defaultly map shows map object, thats why we converting into list

#-------------------#-------------------#-------------------#-------------------#
print("\n")

numbers1 = [10, 20, 30, 40]
numbers2 = [10, 20, 30, 40]

Result_3 = map(lambda x,y : x+y, numbers1, numbers2)
print(list(Result_3))