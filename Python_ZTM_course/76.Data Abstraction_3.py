"""
In Data abstraction we declear two abstract class but we declear definition for one abstract class
"""

from abc import ABC, abstractmethod

class a(ABC):
    @abstractmethod
    def method_1(self):
        pass
    @abstractmethod
    def method_2(self):
        pass


class b(a):
    def method_1(self):
        print("i'm from method_1")

# obj = b() # Here, we did't define for method_2 that's why it will show error.
# obj.method_1() 

# Above method will show error because we did't mention method_2 in class 'b'. so program consider class 'b' also abtraction class.

# overcome the error
# concrete class -->There is no abstract class. 

class b_1(a):
    def method_1(self):
        print("I'm from method_1")
    
    def method_2(self):
        print("I'm from method_2")

obj_1 = b_1()
obj_1.method_1()
obj_1.method_2()
print('\n')

# creating multiple class

class z(a):
    def method_1(self):
        print('From \'z\' class')
    def method_2(self): # here, we want to define all methods otherwise it will show error.
        pass

class z_1(z):
    def method_2(self):
        print('From \'z_1\' class')
    def method_1(self):
        pass
    

obj_z = z()
obj_z_1 = z_1()
obj_z.method_1()
obj_z_1.method_2()
print('\n')

# Using "super()"

class abst(ABC):
    @abstractmethod
    def one(self):
        print("I'm from abstract method")
        pass

class derived(abst):
    def one(self):
        super().one() # super() --> reffer base class('abst' class)
        print("I'm from drived class")

obj_2 = derived()
obj_2.one() # in last program, program will overwrite abstract class print statement. but here using "super()" we can access both print statement.