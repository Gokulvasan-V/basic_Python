"""
A generator function in Python is defined like a normal function, 
but whenever it needs to generate a value, 
it does so with the yield keyword rather than return. If the body of a def contains yield, 
the function automatically becomes a Python generator function. 
"""

"""
Inside the function, when Python see "yield" that time python consider as a Generator.
"""

# normal function

def num():
    return 5
print(num())

# generator function

def num_1():
    yield 5
print(num_1())