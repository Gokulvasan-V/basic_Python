"""
Loops gives us a whole new power when it comes to our machines.
The concept of loops or looping in programming is really, really powerful.
"""
"""
For loops allow us to iterate over anything that has a collection of items .
"""

for items in 'Zero to Mastery':
    print(items)
print('\n')

for items in [1,2,3,4,5,6,7]:
    print(items)
print('\n')

# nested loops
for items in [1,2,3,4,5,6,7]:
    for x in ('a','b','c','d','e','f'):
        print(items,x)
