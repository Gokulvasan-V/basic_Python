class A:
    def __init__(self, value):
        self.value = value
    def __gt__(self, other):
        if(self.value > other.value):
            return True
        else:
            return False
obj1 = A(10)
obj2 = A(30)

if(obj1 > obj2):
    print("object 1 is greater than object2")
else:
    print("object 2 is greater than object 1")

print('\n')
#-------------------#-------------------#-------------------#-------------------#

class A:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):  
        if(self.value < other.value):
            return "object 1 is lesser than object2"
        else:
            return "object 2 is lesser than object 1"
    
                 
object1 = A(2)
object2 = A(3)
print(object1 < object2)

print('\n')
#-------------------#-------------------#-------------------#-------------------#

class A:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        if(self.value == other.value):
            print( "Both are equal")
        else:
            print("Not equal")
object3 = A(9)
object4 = A(9)
object3 == object4