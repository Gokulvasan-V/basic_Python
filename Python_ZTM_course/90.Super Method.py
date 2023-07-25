"""
"super()" method is used to refer to the parent class or superclass. 
It allows you to call methods defined in the superclass from the subclass, 
enabling you to extend and customize the functionality inherited from the parent class.
"""

class a:
    def __init__(self):
        print("i'm from init 'a'")
    def func1(self):
        print("I'm from func_1")

class b(a):
    def __init__(self):
        print("i'm from init 'b'")
    def func2(self):
        print("i'm from func_2")


obj = b() # here, init 'b' will print.
print('\n')
# how to print init 'a', that time we will use "super()" method.


class a:
    def __init__(self):
        print("i'm from init 'a'")
    def func1(self):
        print("I'm from func_1")

class b(a):
    def __init__(self):
        super().__init__()
        print("i'm from init 'b'")
    def func2(self):
        print("i'm from func_2")

obj = b() # using 'super()' method we can use previous class method.
print('\n')


class a:
    def __init__(self):
        print("i'm init 'a'")
    def func_1(self):
        print("i'm func_1")
    
class b:
    def __init__(self):
        print("i'm init 'b'")
    def func_2(self):
        print("i'm func_2")

class c(a,b):
    def __init__(self):
        super().__init__()
        print("i'm init 'c'")

obj = c()