class student:
    def __init__(self,mark1,mark2):
        self.m1=mark1
        self.m2=mark2
    def __add__(self,temp):
        first_stu=self.m1+self.m2
        second_stu=temp.m1+temp.m2
        total=student(first_stu,second_stu)
        return total
    def __sub__(self,temp):
        first_stu=self.m1-self.m2
        second_stu=temp.m1-temp.m2
        total=student(first_stu,second_stu)
        return total
    def __mul__(self,temp):
        first_stu=self.m1*self.m2
        second_stu=temp.m1*temp.m2
        total=student(first_stu,second_stu)
        return total
    def __truediv__(self,temp):
        first_stu=(self.m1+self.m2)/2
        second_stu=(temp.m1+temp.m2)/2
        total=student(first_stu,second_stu)
        return total    
s1=student(10,20)
s2=student(30,50)
add=s1+s2
sub=s1-s2
mul=s1*s2
div=s1/s2

print("addded value:",add.m1, add.m2)
print("subtracted value:",sub.m1, sub.m2)
print("multiplicated value:", mul.m1, mul.m2)
print("average:",div.m1, div.m2)
print('\n')

#-------------------#-------------------#-------------------#-------------------#
