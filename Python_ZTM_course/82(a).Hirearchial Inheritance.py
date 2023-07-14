# Real Time example of Hirearchial Inheritance

# Addition and Subtraction
class add_sub:
    def value(self):
        self.a = 20
        self.b = 10

class Addition(add_sub):
    def add(self):
        print("Added value:", self.a + self.b)


class Subtraction(add_sub):
    def sub(self):
        print("Subtracted value:", self.a - self.b)

plus = Addition()
minus = Subtraction()

plus.value()
plus.add()

minus.value()
minus.sub()