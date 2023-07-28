# here we wil see real time example of 'super()' method.

# finding volume - normal method
class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        print("Rectangle:", self.length * self.breadth)
    
class cube:
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height
        print("Cube:",self.length * self.breadth * self.height)

R = rectangle(2,3)
C = cube(2,3,4)
print('\n')

#-------------------#-------------------#-------------------#-------------------#

# finding volume - using "super()" method.
# NOTE: without inheritance we can't use "super()" method.

class shape():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

class rectangle(shape):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)
        print("Rectangle:", self.length * self.breadth)
    
class cube(shape):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height
        print("Cube:",self.length * self.breadth * self.height)

R_1 = rectangle(3,4)
C_1 = cube(5,6,7)
print('\n')

#-------------------#-------------------#-------------------#-------------------#

class shape():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.res = self.length * self.breadth

class square(shape):
    def __init__(self, length):
        super().__init__(length, length)
        print("Square:",self.res)

class rectangle(shape):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)
        print("Rectangle:",self.res)
    
class cube(shape):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height
        print("Cube:",self.res * self.height)

S_2 = square(2)
R_2 = rectangle(3,4)
C_2 = cube(5,6,7)