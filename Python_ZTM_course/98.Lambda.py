"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, 
but can only have one expression.
"""

"""
Syntax:
(variable) = lambda (argument) : (expression)
"""
message = lambda : print("hello world")
message()

print('\n')
#-------------------#-------------------#-------------------#-------------------#

x = lambda a : a + 10
# in above, 'a' is an argument 'a+10' is an expression
print(x(5))

print('\n')
#-------------------#-------------------#-------------------#-------------------#

# x = lambda a : b + 10 # we don't give 'b' here, whatever we passed as an argument that only we must pass.
# print(x(5))


# print('\n')
#-------------------#-------------------#-------------------#-------------------#
