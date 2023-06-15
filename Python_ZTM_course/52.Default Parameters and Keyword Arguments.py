# Default Parameter
def welcome(name = 'babloo', emoji='❤️'):
    print(f'hellooo {name}{emoji}')

welcome()
welcome('keerthi') # Here i give name only
welcome(emoji='🙌')
print('\n')

# Positional Argument
welcome('Gokulvasan', '😇')
welcome('MuthuRaj', '😉')
welcome('Vimal', '😊')
print('\n')

# Keyword Argument
welcome(emoji='😉',name='MuthuRaj')
welcome(emoji='😊',name='Vimal')
welcome(name='Gokulvasan',emoji='😇')


