# set operation
my_set = {1,2,3,4,5,6}
your_set = {4,5,6,7,8,9,10}

# print(my_set.difference(your_set)) # It's going to find the difference of the first my set with your set.

# # discard --> it removes an element from a set if it is a member.
# my_set.discard(6)
# print(my_set)

# # difference_update --> Remove all elements of another set from this set.
# my_set.difference_update(your_set)
# print(my_set) # differences are removed

# # intersection --> all elements that are in both sets.
# print(my_set.intersection(your_set))
# print(my_set & your_set)

# # isdisjoint --> Return True if two sets have a null intersection. (It means these sets have nothing in common).
# print(my_set.isdisjoint(your_set))

# # union --> all elements that are in either set.
# print(my_set.union(your_set)) # (Or) we have a other method.
# print(my_set | your_set) # | --> means union

# subset --> if all the elements of Set A are also present in Set B.
my_set_2 = {4,5}
print(my_set_2.issubset(your_set))

#superset --> all the elements of set B are the elements of set A.
print(my_set_2.issuperset(your_set))
print(your_set.issuperset(my_set_2))

"""
'difference' and 'difference_update' are same, but difference_update store that difference value in that variable.
"""

"""
If you want to know more,
https://www.w3schools.com/python/python_ref_set.asp
"""