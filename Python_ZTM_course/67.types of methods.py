"""
    Type of methods
    1) Instance Method --> we denote 'self' parameter inside the method
    2) Class Method --> using decorator '@classmethod' without 'self' parameter.
    3) Static Method --> using decorator '@staticmethod' without 'self' parameter
"""

class Subject:
    method = "This is class method"

    def __init__(self,tamil,english,maths):
        self.tamil = tamil
        self.english = english
        self.maths = maths

    def marks(self): # Instance Method (default method)
        total = self.tamil + self.english + self.maths
        return total
    
    @classmethod # Class Method using decorator
    def ClassMethod(cls): # here we need to define one parameter
        return cls.method
    
    @staticmethod # Static Method using decorator
    def StaticMethd(): # here we don't need to pass parameter.
        method = "This is Static Method"
        return method

obj = Subject(95,96,85)
print(obj.marks())
print(obj.english)
print(obj.ClassMethod())
print(obj.StaticMethd())