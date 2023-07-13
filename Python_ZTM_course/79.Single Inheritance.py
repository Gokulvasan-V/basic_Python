"""
Single inheritance enables a derived class to inherit properties from a single parent class, 
thus enabling code reusability and the addition of new features to existing code.
"""

class person: # parent class
    def bio_data(self):
        name = "Gokulvasan"
        age = 24
        gender = "Male"
        print("Employee Name: ", name)
        print("Employee Age: ", age)
        print("Employee Gender: ", gender)

"""
I created one class, i created for another purpose.
I want to add more content but i shouldn't modify 'person' class.
I want to more content including 'person' clas, that time we will use Inheritance concept.
"""

class update_person(person): # child class
    def update_biodata(self):
        city = "Salem"
        state = "Tamilnadu"
        country = "Indian"
        print("Employee City: ", city)
        print("Employee State: ", state)
        print("Employee Country: ", country)


obj = update_person() # Here, we want to create object for "child class".
obj.bio_data()
obj.update_biodata()
print('\n')

obj_2 = person()
obj.bio_data()
#obj_2.update_biodata() # it will show error, because we didn't mention "update_person" class inside the "person" class.