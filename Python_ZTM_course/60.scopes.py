"""
scope simply means What variables do I have access to...?
"""

total = 100 # global scope (or) global variable, in this variable we can access anywhere in this program.
print(total)

def func_scop():
    total_1 = 100 # functional scope (or) functional variable, this type of variable we can access only inside this function only we can't access outside of this function.

#print(total_1) # it will show error.
