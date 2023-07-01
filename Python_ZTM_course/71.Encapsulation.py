"""
# Encapsulation is the binding of data and functions that manipulate that data.
# We're able to encapsulate the functionality of our player character by having name and age data(methods) or attributes
# Someone wants to change our code means 'Encapsulation' will work that time. That change won't work in that time by using 'Encapsulation'.
"""

class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age

player1 = PlayerCharacter('Gokul',24)
print('Player_1 name:',player1.name)
print('Player_1 age:',player1.age)
print('\n')

player2 = {'name':'gokul','age':23}
print('Player_2 name:',player2['name'])
print('Player_2 age:',player2['age'])
print('\n')

player3 = PlayerCharacter('GV',24)
player3.name = 'Hello' # using 'Encapsulation' we can neglect this type Overwritting.
print('Player_3 name:',player3.name)
print('Player_3 age:',player3.age)




"""
If wants to know more,
https://www.geeksforgeeks.org/encapsulation-in-python/
"""
