# here we will see 'super()' method in single inheritance.

class test:
    def method_1(self):
        print("Hai... I'm from Method 1")

class test_2:
    def method_2(self):
        test.method_1(self) # here we called from 'method_1'.

t = test_2()
t.method_2()
print('\n')
#------------#------------#------------#------------#------------#------------#

class test:
    def method_1(self):
        print("Hai... I'm from Method 1")

class test_2(test):
    def method_2(self):
        test.method_1(self) # here we called from 'method_1'.

t2 = test_2()
t2.method_2()
print('\n')
#------------#------------#------------#------------#------------#------------#

class test:
    def method_1(self):
        print("Hai... I'm from Method 1")

class test_2(test):
    def method_2(self):
        super().method_1()
        print("Hai... I'm from Method 2")
t3 = test_2()
t3.method_2()
print('\n')
#------------#------------#------------#------------#------------#------------#

class test:
    def method_1(self):
        print("Hai... I'm from Method 1")
    def method_2(self):
        print("Hai... I'm from Method 2")
    
class test_2(test):
    def method_3(self):
        super().method_1()
        super().method_2()
        print("Hai... I'm from Method 3")

t4 = test_2()
t4.method_3()
print('\n')
#------------#------------#------------#------------#------------#------------#

class person_1:
    def detial_1(self, name):
        print("Person_1 name:", name)

class person_2(person_1):
    def detial_2(self):
        super().detial_1("Gokulvasan") # In 'detial_1' method we passed one parameter, so we mentiond here. 

t5 = person_2()
t5.detial_2()