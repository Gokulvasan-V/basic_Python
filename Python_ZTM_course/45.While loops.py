"""
while loop is a little different in that we say while a condition is happening loop will execute.
this is what we call an infinite loop.
"""

i = 0

# while i<50:
#     print(i) #what happened was while this was true, we print it.
#     #i += 1
print('\n')

"""
to jump out of a wild loop, you can either turn the condition false or you can break out of the
"""

while i<50:
    print(i) 
    i += 2
else:
    print('While loop comleted.')

print('\n')

j=0
while j<50:
    print(j)
    j += 2
    break # we can add break also, it stop after 1st execution.
else:
    print('While loop comleted.') # Here, else part won't print because after break statement program will stop.