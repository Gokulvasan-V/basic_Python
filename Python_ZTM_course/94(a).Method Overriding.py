# Polymorphism using Inheritance and Method Overriding

# already we saw this code (in 94)
class a:
    def detials(self):
        print("I'm from class a")

class b(a):
    def detials(self):
        print("I'm from class b")
        super().detials()

class c(b):
    def detials(self):
        print("I'm from class c")
        super().detials()

obj = c()
obj.detials()

print('\n')
#-------------------#-------------------#-------------------#-------------------#

class sheela:
    def speak(self):
        return "I'm Sheela"
    
class sakthi(sheela):
    def speak(self):
        return "I'm Sakthi"
    
class shiva(sakthi):
    def speak(self):
        return "I'm Shiva"
    
obj_1 = sheela()
obj_2 = sakthi()
obj_3 = shiva()

for i in (obj_1, obj_2, obj_3):
    print(i.speak())

print('\n')
#-------------------#-------------------#-------------------#-------------------#

# here, i creating three class inside the single object.
objj = (sheela(), shiva(), sakthi())

for i in objj:
    print(i.speak())
