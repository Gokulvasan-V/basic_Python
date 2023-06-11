"""
What I want you to do is using looping to loop over this iterable list and sum up the total of the list.
"""

my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0

for i in my_list:
    counter += i
    print(counter) # it will show one by one adding operation.

print('\n')
print(counter)
print('\n')


"""
if you moved the 'counter' to zero inside the loop, well every time the counter would be reset to zero.
so that by the time we get to ten, counter would be zero.
"""
for i in my_list:
    counter = 0
    counter += i
    print(counter)

print('\n')
print(counter)
