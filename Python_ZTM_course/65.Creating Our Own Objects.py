
class PlayerCharacter:
    def __init__(self, name): # method 1
        self.name = name

    def run (self): # method 2
        print('Run')
        return 'done' # if we forgot to add return means program will show 'None'.

player_1 = PlayerCharacter('Gokul')
print(player_1) # shows the memory location.
print(player_1.name) # it will print the 'name' variable.
print('\n')

player_2 = PlayerCharacter('Tom')
print(player_2.name)
print('\n')

print(player_1.run())
print('\n')

help(player_1) # it shows the blueprint of 'Player_1' object