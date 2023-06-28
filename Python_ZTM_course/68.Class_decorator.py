class PlayerCharacter:
    membership = True # Class Object Attribute (variable)
    def __init__(self, name,age):
        if (self.membership):
            self.name = name # attribute (variable)
            self.age = age

    def shout (self):
        print(f'Your name is {self.name}')
    
    @classmethod
    def adding_things(cls, num1, num2): # in '@classmethod' we must pass 'cls' as a parameter
        return num1 + num2
    """
    we would use something like static method where we don't care anything about the class state. 
    """
    @staticmethod
    def adding_things2(num1, num2): # in '@classmethod' we must pass 'cls' as a parameter
        return num1 + num2

player1 = PlayerCharacter('tom', 20)

# @classmethod
print(player1.adding_things(5,7))
# we can access
print(PlayerCharacter.adding_things(8,9))

