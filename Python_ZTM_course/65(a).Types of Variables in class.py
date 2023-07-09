"""
types of variables in class

1) Class (or) Static variable --> define inside the class
2) Instance variables --> define inside the method(function)
"""

class car:
    wheels = 4 # Class variable

    def __init__(self):
        self.mileage = 10 # Instance variables
        self.brand = 'Jaguar ' # Instance variables

c1 = car()
c2 = car()

# instance variable
print(c1.brand, c1.mileage)
print(c2.brand, c2.mileage)
print('\n')

# changing "instance variable" value.
c1.mileage = 8 # we can change the value, it won't affect the entire class.
c2.brand = 'Volvo' # here, i changed only c2 object value. it won't affect entire class
print(c1.brand, c1.mileage)
print(c2.brand, c2.mileage) # c2 object didn't affect here.
print('\n')

# class variable
print(c1.brand, c1.mileage, c1.wheels)
print(c2.brand, c2.mileage, c2.wheels)
print('\n')

# changing "class variable" value.
car.wheels = 5 # we can change the value, it will affect the entire class.
print(c1.brand, c1.mileage, c1.wheels) # here, changed value affected entire class.
print(c2.brand, c2.mileage, c2.wheels)