"""
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
"""

"""
Decorator :
----------

1) Function Decorator
2) Class Decorator
"""

"""
Function Decorator :
-------------------

1) Single Function Decorator
2) Multiple Function Decorator

Types of Function Decorator :
-----------------------------
1) With Argument
2) Without Argument
"""

# 1) Single Function Decorator

def Upper_string(ref):
    def process():
        data = ref()
        return data.upper()
    return process

@Upper_string # Decorator
def Myfunc():
    return 'Welcome to Python'

result = Upper_string(Myfunc)
print(result.__name__) # it will show the function name

result_1 = Upper_string (Myfunc)
print(result_1())

print('\n')

# (or) we use @Upper_string(function name) above the changable function.
print(Myfunc())

print('\n')

# 2) Multiple Function Decorator

def Upper_string(ref):
    def process():
        data = ref()
        return data.upper()
    return process

def Split(ref):
    def process():
        data = ref()
        return data.split()
    return process

@Split
@Upper_string # Decorator
def Myfunc_2():
    return 'Welcome to Python programming language'

print(Split(Myfunc_2))
print(Myfunc_2())