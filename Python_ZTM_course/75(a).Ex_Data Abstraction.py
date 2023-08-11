from abc import ABC, abstractmethod

# here, we created what we want.
class a(ABC):
    @abstractmethod
    def method1(self):
        print("Hello")
    
    @abstractmethod
    def method2(self):
        print("Hii")

# we already hidded the code, we exsicute here  
class b(a):
    def method1(self):
        super().method1()
    def method2(self):
        super().method2()
        
obj = b()
obj.method1()
obj.method2()