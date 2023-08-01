
"""
example:

using polymorphism, method overriding, inheritance.
"""

class vehicle:
    def __init__(self, name, colour, price):
        self.name = name
        self.colour = colour
        self.price = price

    def show(self):
        print("Detials:", self.name, self.colour, self.price)

    def speed(self):
        print("Vehicle max Speed is 100")

    def gear(self):
        print("Scooty has no gear")

class car(vehicle):
    def speed(self):
        print("Car max speed is 240")

    def gear(self):
        print("Car has Gear")

Car = car('kwid', 'Red', '8L')
Car.show()
Car.speed()
Car.gear()

print('\n')
#-------------------#-------------------#-------------------#-------------------#

ve = vehicle("Suzuki", "Silver", "1L")
ve.show()
ve.speed()
ve.gear()

print('\n')
#-------------------#-------------------#-------------------#-------------------#

class scooty(vehicle):
    def speed(self):
        super().speed()

    def gear(self):
        super().gear()

Sc = scooty("Suzuki", "Black", "1.5 L")
Sc.show()
Sc.speed()
Sc.gear()