""""
In Python, individual values can evaluate to either True or False.

The Basis rules are:

1) Values that evaluate to False are considered Falsy.
2) Values that evaluate to True are considered Truthy.
"""

# number = 7
# if number:
#   print(number)

number = 0
if number:
  print(number) # it won't show anything.
  
# Falsy
"""
Falsy Values Includes:

1) Sequences and Collections:
Empty lists []
Empty tuples ()
Empty dictionaries {}
Empty sets set()
Empty strings ” “
Empty ranges range(0)

2) Numbers: Zero of any numeric type.
Integer: 0
Float: 0.0
Complex: 0j

3) Constants:
None
False

Falsy values were the reason why there was no output in our initial example when the value of number was zero.
"""

# Truthy
"""
Truthy Values Includes:

1) Non-empty sequences or collections (lists, tuples, strings, dictionaries, sets).
2) Numeric values that are not zero.
3) Constant: True

This is why the value of a printed in our initial example because its value of a number was 7(a truthy value)
"""

bool(7)
# True
  
bool(0)
 #False
    
bool([])
# False
  
bool({7,4})
#True
  
bool(-4)
# True
  
bool(0.0)
# False
  
bool(None)
# False
  
bool(1)
#True
  
bool(range(0))
# False
  
bool(set())
# False
  
bool([1,2,3,4])
# True



"""
if you want to know more:

https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false
"""