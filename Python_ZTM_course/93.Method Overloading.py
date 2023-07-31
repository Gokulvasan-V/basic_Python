"""
Two or more methods have the same name but different numbers of parameters or different types of parameters, or both. 
These methods are called overloaded methods and this is called method overloading.

Like other languages (for example, method overloading in C++) do, 
python does not support method overloading by default. 
But there are different ways to achieve method overloading in Python. 
"""

class a:
    def fun(self,a):
        print(a)
    def fun(self, a, b):
        print(a+b)
    def fun(self, a, b, c):
        print(a+b+c)

obj = a()
obj.fun(10,20,30)
# obj.fun(10) #ERROR --> this is method overloading, 1st we mentioned method with single parameter. but here, don't work.
# obj.fun(10, 20) #ERROR
print('\n')

#-------------------#-------------------#-------------------#-------------------#

# Method Overloading

class a:
    def fun(self, a=None, b=None, c=None):
        if (a!=None and b!=None and c!=None):
            print(a+b+c)
        elif (a!=None and b!=None):
            print(a+b)
        else:
            print(a)

obj_2 = a()
obj_2.fun(10,20,30)
obj_2.fun(10,20)
obj_2.fun(10)