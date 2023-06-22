"""
everything here is an object because in Python, everything is built by this class keyword.

Objects have methods like these and attributes that you can access with the "DOT(.)" method.

This OOPs is a paradigm, a way to think about our code, a way for us to structure.
"""

"""
Concepts in OOP's
1) Class & Object
# Class --> collections of variables and functions.
# Object --> Inside the 'Class', Every individual function call is called as 'object'.
2) Constructor
3) Encapsulation
4) Polynorphism
5) Inheritance
6) Data Abstraction
"""


# Ex: Class & Object

class Myclass: #class
    a = 10 # variable
    def Myfunc(self): # function
        print("This is class & object")

obj = Myclass() # object (we can access above class(Myclass) in the name of 'obj')
obj.Myfunc() # here we acess 'Myfunc' function with the 'obj' object. 
print(obj.a) # here i access 'a' variable with 'odj' object.