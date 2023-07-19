
def person (name, **value): # **kwargs --> keyword argument
    print("Name:", name)
    print("Age:", value['age'])
    print("City:", value['city'])
    print("M.No:", value['m_no'])

person("Gokul", age=24, city='Salem', m_no=9524703012)

print('----'*4)

class test:
    def __init__(self,name, **value):
        print("Name:", name)
        print("Age:", value['age'])
        print("City:", value['city'])
        print("M.No:", value['m_no'])

obj = test("Gokul", age=24, city='Salem', m_no=9524703012)
print('\n')

# Finding Area of Triangle 

print("# Finding Area of Triangle")

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
        self.area = (self.base * self.height)*0.5
        print("Area of Triangle", self.area)

obj = Triangle(7,10)

print('----'*4)

class Triangle_2:
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def area_of_triangle(self):
        self.area = (self.base * self.height)*0.5
        print("Area of Triangle", self.area)

obj_2 = Triangle_2(7,10)
obj_2.area_of_triangle()