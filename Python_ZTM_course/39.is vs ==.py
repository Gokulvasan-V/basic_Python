
# == --> double equals checks for equality or equality of value.

print(True == 1)
print(False == 0)
print("" == 1)
print("1" == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
print([1,2,3] == (1,2,3))
print([1,2,3] == [1,2,3])
print("\n")


# is --> a keyword and python. 


print(True is 1)
print(False is 0)
print("" is 1)
print("1" is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])
print([1,2,3] is (1,2,3))
print([1,2,3] is [1,2,3])
"""
I get false for everything.

So what's the difference here...?

# Equals to (==) --> checks for the equality in value.
    such as One, two, three. that's has the same value as one, two, three In a list.
    ex: [1,2,3] == [1,2,3]
# is --> actually checks, If the location in memory where this value is stored is the same.
    it's going to check, hey, is this in the same memory space, same bookshelf as that one...?
"""
print(True is 1) # here, 'true' is not stored in 'one' location
print(True is True)

print('1' is 1) #  the 'one string' isn't only in 'one' place in memory.
print('1' is '1')

print([] is []) # I still get false, both are stored in different different location.
# these are two completely different lists.

print(10 is 10.0) # both are stored in different different location.
print(10 is 10)

print([1,2,3] is [1,2,3]) # Every time we create it, it's created in a new location.
a = [1,2,3]
b = [1,2,3]
print(a is b) # this where 'a' points is in a different place than where 'b' points.