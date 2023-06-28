
"""
Type of Function:
-----------

1) Nested Function
2) Function as a parameter
3) Function as a refference
4) Function returns another function 
"""

def Outer_function():
    msg1 = 'Welcome to'
    def Inner_function(): # Nested Function
        msg2 = 'Python'
        out = msg1 + msg2
        return out
    return Inner_function # Function returns another function.

obj = Outer_function()
print(obj()) # Function as a Refference


# 4) function as a parameter.
def Myfunc1():
    print('This is my Function 1')

def Myfunc2(ref):
    print('This is Function 2')
    print(ref.__name__) # print the name
    ref()

Myfunc2(Myfunc1)