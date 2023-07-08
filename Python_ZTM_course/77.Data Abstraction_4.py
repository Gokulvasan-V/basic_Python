from abc import ABC, abstractmethod

class sides(ABC):
    @abstractmethod
    def number(self):
        pass

class triangle(sides):
    def number(self):
        print('I have 3 sides')

class square(sides):
    def number(self):
        print('I have 4 sides')

class pentagon(sides):
    def number(self):
        print('I have 5 sides')

t = triangle()
t.number()

s = square()
s.number()

p = pentagon()
p.number()