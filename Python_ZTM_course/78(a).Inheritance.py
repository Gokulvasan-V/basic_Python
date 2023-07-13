
class User(): # parent class
    def sign_in(self):
        print("Logged In")
    
class Wizard(User): # child class of 'user' class
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"Attacking with power of {self.power} ")

class Archer(User): # child class of 'user' class
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f"Attacking with arrows: arrows left- {self.num_arrows} ")

wizard_1 = Wizard("GokulVasan", 50)
Archer_1 = Archer("GV", 200)

wizard_1.attack()
wizard_1.sign_in() # both classes has 'sign-in' method
print("\n")

Archer_1.attack()
Archer_1.sign_in() # both classes has 'sign-in' method
