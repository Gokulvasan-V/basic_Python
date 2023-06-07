"""
Sets are simply unordered collections of unique objects.
"""

my_set = {1,2,3,4,5,6,7,8,9,5,6}
print(my_set)

# Here, there's no real order to it. that's why we are calling unordered collection.
"""
It only returns the unique sets or unique items you see in a set There's no duplicates.
Everything has to be unique.
"""

my_set.add(10)
my_set.add(1) # i can't add 1 because 1 already exist. 
print(my_set)

# remove duplicates in list

my_list = [1,2,3,4,5,6,5,4,3,2,1]

print(set(my_list))

# Here, we can use string also.
my_set_2 = {'hello', 'hii', 'hii', 'hiii'}
print(my_set_2)

"""
Set object does not support indexing.
"""
#print(my_set[0])

print(1 in my_set)
print(len(my_set)) #it only counts the unique things.


print(list(my_set)) # it will print only unique values.
set_copy = my_set.copy()
print(set_copy)
