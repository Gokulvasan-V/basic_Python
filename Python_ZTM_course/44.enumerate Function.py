"""
Enumerate --> it's going to take an iterable object and gives you an index counter and the item that index.
"""

for i,char in enumerate('Hellloooo'):
    print(i, char)
print('\n')

for i, char in enumerate([1,2,3,4,5,6,7,8,9,10]):
    print(i, char) # here, I'm able to use and access the index number of the item as well.
print('\n')

for char in enumerate({1,2,3,4,5,6,7,8,9,10},start=1):
    print(char)