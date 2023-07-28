# here we will see 'super()' method in Multi-level inheritance.

# Normal Multi-level inheritance
class A:
    def method_1(self):
        print("From class 'A'")

class B(A):
    def method_2(self):
        print("From class 'B'")

class C(B):
    def method_3(self):
        print("From class 'C'")

# without "super()" method we want to create object for all methods.
obj = C()
obj.method_3()
obj.method_2()
obj.method_1()
print('\n')

# Normal Multi-level inheritance with "super()"
class A:
    def method_1(self):
        print("From class A")

class B(A):
    def method_2(self):
        print("From class B")
        super().method_1()

class C(B):
    def method_3(self):
        print("From class C")
        super().method_2()

obj_2 = C()
obj_2.method_3() # here we created one object, and we need not to be call methods for all.
print('\n')

#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#

class X:
    def __init__(self):
        print("Class 'X'- Construtor")
    def method_1(self):
        print("Class 'X' - From method_1")

class Y(X):
    def __init__(self):
        print("Class 'Y' - Construtor")
        super().__init__()
    def method_2(self):
        print("Class 'Y' - From method_2")
        super().method_1()

class Z(Y):
    def __init__(self):
        print("Class 'Z' - Construtor")
        super().__init__()
    def method_3(self):
        print("Class 'Z' - From method_3")
        super().method_2()

obj_3 = Z()
obj_3.method_3()
print('\n')

#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#

# How super will work...? decending to accending(class Z to class X)
# See addiction order.

class X:
    def __init__(self):
        print("Class 'X'- Construtor")
    def method_1(self,b):
        print("Class 'X' - From method_1",b)

class Y(X):
    def __init__(self):
        print("Class 'Y' - Construtor")
        super().__init__()
    def method_2(self,b):
        print("Class 'Y' - From method_2",b)
        super().method_1(b+1)

class Z(Y):
    def __init__(self):
        print("Class 'Z' - Construtor")
        super().__init__()
    def method_3(self,b):
        print("Class 'Z' - From method_3",b)
        super().method_2(b+1)

obj_4 = Z()
obj_4.method_3(1)

