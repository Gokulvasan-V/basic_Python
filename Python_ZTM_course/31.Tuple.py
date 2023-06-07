
my_tup = (1,2,3,4,5,6,7,8,9,10)
new_tup = my_tup[1:5] # slice 
print(new_tup)

x,y,z,*others = (1,2,3,4,5,6,7)

print(x)
print(y)
print(z)
print(others)

my_tup_2 = (1,2,3,4,5,6,7,8,9,10,2,8,2,2)
print(my_tup_2.count(2)) # how many two occurs in the tuple
print(my_tup_2.index(6)) # What's the index of six?

print(len(my_tup_2)) # find the length.

"""
a tuple has only two methods that we care about count and index.
https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/15837206#content
"""