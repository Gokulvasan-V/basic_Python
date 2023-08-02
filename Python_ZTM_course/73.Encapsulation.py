# Setter and Getter Methods 

class detial:
    def setname(self, n): # Setter Method --> Here we set the method
        self.__name = n
    def getname(self): # Getter Method --> Here we get (or) receive  the method
        return self.__name
    def dispaly(self):
        print("Student Name:", self.getname()) # 'self' means current class name

obj = detial()
obj.setname("Sakthi")
obj.dispaly()

print('\n')
#-------------------#-------------------#-------------------#-------------------#

class detial_1:
    def setname(self, n):
        self.__name = n
    def getname(self):
        return self.__name
    
    def setage(self, a):
        self.__age = a
    def getage(self):
        return self.__age
    
    def dispaly(self):
        print("Student Name:", obj.getname())
        print("Student age:", self.__age)

obj_1 = detial_1()
obj_1.setname("Sakthi")
obj_1.setage(25)
obj_1.dispaly()
    