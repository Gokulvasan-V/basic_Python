"""
Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes.
When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, 
then the method in the subclass is said to override the method in the super-class.
"""

class a:
    def detials(self):
        print("I'm from class a")

obj = a()
obj.detials()

print('\n')
#-------------------#-------------------#-------------------#-------------------#

class a_1:
    def detials(self):
        print("I'm from class a")

class b_1(a_1):
    pass

obj_1 = b_1()
obj_1.detials()

print('\n')
#-------------------#-------------------#-------------------#-------------------#

class a_2:
    def detials(self):
        print("I'm from class a")

class b_2(a_2):
    def detials(self):
        print("I'm from class b")
        super().detials()

obj_2 = b_2() # this is called method overriding.
obj_2.detials()
print(b_2.__mro__)

print('\n')
#-------------------#-------------------#-------------------#-------------------#

class a_3:
    def detials(self):
        print("I'm from class a")

class b_3(a_3):
    def detials(self):
        print("I'm from class b")
        super().detials()

class c_3(b_3):
    def detials(self):
        print("I'm from class c")
        super().detials()

obj_3 = c_3()
obj_3.detials()
print(b_3.__mro__)
print(c_3.__mro__)



"""
Want to know more,
https://www.geeksforgeeks.org/method-overriding-in-python/
"""