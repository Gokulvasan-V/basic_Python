"""
iterator is an object that allows you to iterate over collections of data, 
such as lists, tuples, dictionaries, and sets. 
Python iterators implement the iterator design pattern, 
which allows you to traverse a container and access its elements.
"""

lst = [1,2,3,4,5]

# Here, I want to access elements one by one. in this situation we use indexing (or) looping.

Lst = ["hii", "Hello", "How are you", "python", "happy learning"]
print(Lst[0])
print(Lst[1])
print(Lst[2])
print(Lst[3])
print(Lst[4])

# (or)
print('\nFor loop:')

for m in Lst:
    print(m)

# here we using while
print('\nWhile loop:')

i = 0
while i<len(Lst):
    print(Lst[i])
    i+=1

# this while loop won't applicable for set (set don't allow indexing)

print('\n')
#-------------------#-------------------#-------------------#-------------------#

# we access using "iter" method.

List_1 = [1,2,3,4,'python', 'R language']
# we must convert to 'iter' method.
print(iter(List_1)) # it will show the object.
it = iter(List_1)

# here, we access all list elements without looping.
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) # it will show error, because there is no elements after this.

print('\n')
#-------------------#-------------------#-------------------#-------------------#

List_2 = [1,2,3,4,'python', 'R language']
ite = iter(List_2)
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())


