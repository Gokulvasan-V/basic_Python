
class PlayerCharacter:
    membership = True # Class Object Attribute
    def __init__(self, name,age):
        if (self.membership):
            self.name = name # attribute
            self.age = age

    def run (self):
        print(f'Your name is {self.name}')
        
player_1 = PlayerCharacter('Gokul',24)

player_2 = PlayerCharacter('Tom',34)

print(player_1.membership) # all the players have membership set to true.
print(player_2.membership)
print('\n')

print(player_2.name)
print('\n')

print(player_1.run())

"""
Class object attribute is static, it won't change when we use in other methods.
"""