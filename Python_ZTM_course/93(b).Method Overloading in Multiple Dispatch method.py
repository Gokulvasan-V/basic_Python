
"""
Multiple dispatch (aka multimethods, generic functions, and function overloading) is choosing which among several function bodies to run, depending upon the arguments of a call.
"""

from multipledispatch import dispatch

@dispatch(int, int)
def add(a,b):
    return a+b

@dispatch(int, int, int)
def add(a,b,c):
    return a+b+c

@dispatch(int)
def add(a):
    return a

print(add(10))
print(add(10,20))
print(add(10,20,30))

print('\n')
#-------------------#-------------------#-------------------#-------------------#

class A:
    @dispatch(int, int)
    def add(a,b):
        return a+b

    @dispatch(int, int, int)
    def add(a,b,c):
        return a+b+c

    @dispatch(int)
    def add(a):
        return a
    
obj = A()
print(obj.add(10,20,30)) # in our code we used 'return' that's why we use 'print' here.
print(obj.add(10,20))
print(obj.add(10))

print('\n')
#-------------------#-------------------#-------------------#-------------------#

# Here, we using multiple operations in single method name.

class B:
    @dispatch(int, int)
    def add(a,b):
        return a*b

    @dispatch(int, int, int)
    def add(a,b,c):
        return a+b+c

    @dispatch(int)
    def add(a):
        return a/2
    
    @dispatch(str, str)
    def add(a, b):
        return a+b
    
    @dispatch(float, float)
    def add(a,b):
        return a+b
    
obj_2 = B()
print(obj_2.add(10,20,30)) # in our code we used 'return' that's why we use 'print' here.
print(obj_2.add(10,20))
print(obj_2.add(10))

#string
print(obj_2.add("hello,", " welcome"))

# float
print(obj_2.add(1.5, 2.5))
print(obj_2.add(1.5, 3.0)) # Here, You must mention 'float'.

