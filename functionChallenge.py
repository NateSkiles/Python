import random

mySentence = "'s favorite instrument is the "

instrumentList = ['Bagpipes', 'Kazoo', 'Saxophone', 'Acoustic Guitar', 'Flute', 'Steel Pan',
                  'Viola', 'Dums', 'Guitar', 'Bells', 'Accordion', 'Keyboard', 'Trumpet']

#instrument function, pick random instrument 
def favorite_instrument(name):
        msg = '{0} {1} {2}'.format(name, mySentence, random.choice(instrumentList)) #random.choice selects an item from the list at random
        return(msg)
    
#users name
def get_name():
    go = True
    while go:
        name = input('What is your name?:   ')
        if name == '':
            print('You need to provide a name')
        else:
            go = False
    return name

name = get_name()

print(favorite_instrument(name))
