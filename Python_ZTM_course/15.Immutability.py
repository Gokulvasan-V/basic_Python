"""
immutable --> we can't chenge the value
strings are immutable.
"""

hello= '0123456789'

print(hello[0])
print(hello[5])
print(hello[-5])

#print(hello[3]='9')
#print(hello[3]=9)

"""
The only way that I can remove this or change this is to completely reassign the value.
"""

hello='123456789'
print(hello)
print(hello[3])
