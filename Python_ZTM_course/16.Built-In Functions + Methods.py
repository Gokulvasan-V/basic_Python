# we already known

# str()
# int()
# float()
# print()
# len()

print(len("hellooooo")) #length doesn't start at zero.
        #  123456789

greet= 'have a great day'
print(greet[0:len(greet)]) #it print upto our length of string.

"""
Python also have "Methods"
# Methods are similar to functions
# But they are owned by something.
"""

"""
for example, In Python we have string methods.
So these are methods or actions that only strings can perform.

String Methods --> https://www.w3schools.com/python/python_ref_string.asp
these are methods that we can use specifically for strings and methods have a special syntax

"""

# .format also a method

print(greet.upper())
print(greet.capitalize())
print(greet.find('day')) # it show the staring of the given word
print(greet.replace('day','morning'))

print(greet) # we can't change the stings, bcz strings are immutable.

"""
If you want to know more
Few built-in functions -->  https://docs.python.org/3/library/functions.html

"""