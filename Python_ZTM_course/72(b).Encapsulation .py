# Protected Variable

class detial:
    _name = "gokul"
    _rollno = 14225421

    def display(self):
        print("Name:", self._name)
        print("Roll:", self._rollno)
    
obj = detial()
obj.display()

print('\n')
#-------------------#-------------------#-------------------#-------------------#

class base:
    def __init__(self):
        self._name = "Sakthi"

class derived(base):
    def __init__(self):
        base.__init__(self)
        print("Calling from derived class:", self._name)
        self._name = "Shiva"
        print("Modified name:", self._name)

obj_1 = derived()
obj_2 = base()
print("Accessing protected member of 'obj_1'", obj_1._name)
print("Accessing protected member of 'obj_2'", obj_2._name)
