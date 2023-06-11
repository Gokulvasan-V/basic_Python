"""
it produces a sequence of integers from start to stop.
"""

print(range(100)) # it gives you a default of zero to whatever you give it.
print('\n')

for i in range(10):
    print(i)
print('\n')

for i in range(10):
    print("email list: ")
print('\n')

"""
>> range also comes with a third parameter.
>> And what that is is the step over.
>> So if I do two and by the way, default is one here, if I do two.
    It jumps from 0 to 10 by two.
"""

for i in range(0,10,2): #(start, stop, stepover)
    print(i)
print('\n')

for i in range(10,0,-1):
    print(i) # It's going to go in the opposite direction.
print('\n')

for i in range(10,0,-2):
    print(i)