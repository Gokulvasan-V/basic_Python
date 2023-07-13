"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class --> is the class being inherited from, also called base class.

Child class --> is the class that inherits from another class, also called derived class.
"""

"""
Types of Inheritance:

1) Single Inheritance
2) Multiple Inheritance
3) Multi-level Inheritance
4) Hybrid Inheritance
5) Hirarical Inheritance
"""

# Example of Single Inheritance

class parent:
    def function_1(self):
        print("Hello i'm from parent class")

# Here, i'm acessing 'parent' class inside the 'Child' class.
class child(parent): # Single Inheritance
    def function_2(self):
        print("Hello, i'm from child class")

obj = child() # here, i created object for 'child' class
obj.function_1() # In the 'child' class i accessed 'parent' class.
obj.function_2()





"""
Wants to know more,
https://www.geeksforgeeks.org/types-of-inheritance-python/
"""