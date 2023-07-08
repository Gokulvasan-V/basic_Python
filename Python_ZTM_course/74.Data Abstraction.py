"""
Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user.

That enables the user to implement even more complex logic on top of the provided abstraction without understanding or even thinking about all the hidden background/back-end complexity.
"""

"""
In python we can't implement abstraction directly. we want to use "abs" and "abstractmethod" 
"""

# this is normal class and normal method.
class a: 
    def method_1(self):
        print("i am from method 1")

obj = a() # object
obj.method_1()
print('\n')



# Implement Abstract class

from abc import ABC, abstractmethod

class a(ABC): # ABC --> abstract class (we mentioned abstract class)
    @abstractmethod # we mentioned abstract method using decorator.
    def method_1(self):
        print("i am from method 1")

# it will show error (When we create object for abstract class that time python will show error, without object it will print properly.)
# obj = a() # in abstract class we can't create object
# obj.method_1()


# we will code abstract method like tis
class a(ABC):
    @abstractmethod
    def method_2(self): # here we declear method but we didn't define any logic.
        pass

# here only we must to define what we want in abstract class.
class b(a): # here we Inherited class 'a'
    def method_2(self):
        print("i am from class b & method 2")

obj_1 = b() # object
obj_1.method_2()