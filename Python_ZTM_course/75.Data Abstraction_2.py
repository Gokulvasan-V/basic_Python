"""
Inside the Data abstraction we declear another normal method(function). 
"""

from abc import ABC, abstractmethod

# Abstract Class inside normal function
class a(ABC):
    @abstractmethod
    def method_1(self):
        print("I'm from Class A" )
        pass
    def method_2(self): # Normal method
        print("I'm from method 2")

class b(a):
    def method_1(self):
        print("I'm from class 'b'")

obj=b()
obj.method_1() # Here function will overwrite the print statement.
obj.method_2() # Here, We access 'a' class 'method_2' in class 'b'.

