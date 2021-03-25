

mySentence = ' loves the color'

colorList = ['green', 'blue', 'red', 'pink', 'teal']


# Create a funtion
def color_function(name):
    lst = []
    for i in colorList:         # for i in color list print out each value
        msg = "{0} {1} {2}".format(name, mySentence, i)
        lst.append(msg)
    return lst


def get_name():
    go = True
    while go:
        name = input('What is your name?    ')
        if name == "":
            print('You need to provide your name')
        elif name == 'Sally':
            print('Sally, you may not use this software')
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()
