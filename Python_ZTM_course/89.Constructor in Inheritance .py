class a:
    def __init__(self):
        print("i'm from init 'a'")
    def func1(self):
        print("I'm from func_1")

class b(a):
    def func2(self):
        print("i'm from func_2")


#obj = b()

class c(b):
    def __init__(self):
        print("i'm from init 'c'")
    def func3(self):
        print("I'm from func_3")


obj_2 = c() # 'a' constructor will overwrite, when we add new constructor.
obj_2.func1()