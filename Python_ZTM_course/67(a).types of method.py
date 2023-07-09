
# instance class --> Instance variable work with instance class
# if you working with instance variable you define 'self' parameter
class students:
    school = 'Gokul school'
    
    def __init__(self,m1,m2,m3): # Instance variable
        self.m1 = m1 
        self.m2 = m2
        self.m3 = m3

    # instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

s1 = students(85,96,89)
s2 = students(100,97,99)

print(s1.avg())
print(s2.avg())
print('\n')

#--------#--------#--------#--------#--------#--------#--------#--------#

# Class method --> Class variable work with Class method
# if you working with Class variable you define 'cls' parameter


class students_2:
    school = 'Gokul school' # class variable
    
    def __init__(self,m1,m2,m3): # Instance variable
        self.m1 = m1 
        self.m2 = m2
        self.m3 = m3

    # instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    #class method
    @classmethod # without using decorator it will show error.
    def info(cls):
        return cls.school
    
print(students_2.info()) # if we change the school name it will affact all the methods.
print('\n')

#--------#--------#--------#--------#--------#--------#--------#--------#

# Static method --> we don't know what method we want that time we will use static method.
# if you want a method, which has nothing to do with instance variable, which has nothing to do with class variable we want to somthing extra.



class students_3:
    school = 'Gokul school' # class variable
    
    def __init__(self,m1,m2,m3): # Instance variable
        self.m1 = m1 
        self.m2 = m2
        self.m3 = m3

    # instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    # class method
    @classmethod
    def info(cls):
        return cls.school
    
    # static method
    @staticmethod
    def static_method(): # no need to pass any parameter
        return 'This is from static class'

print(students_3.static_method())