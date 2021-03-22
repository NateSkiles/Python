

num1 = 12

if num1 == 12:
    print('num1 is equal to 12')
else:
    print('num1 is not equal to twelve')



num2 = 12

if num2 == 14:
    print('Num2 is equal to Twelve')
elif num2 < 12:             # else if statement
    print('num2 is less than twelve')
else:
    print('num2 is not equal to twelve')


num3 = 12
key = False # can set a condition nested in a if statement

if num3 == 12:
    if key:
        print('Num2 is equal to Twelve')
    else:
        print('num3 is equal to twleve and they have the key')
elif num3 < 12:
    print('num2 is less than twelve')
else:
    print('num2 is not equal to twelve')


# My if statement

num4 = 18
usa = False
if num4 >=  21:
    print('Lets grab a pint')
elif num4 >= 18 and usa == False:
    print('You can drink, but not in this conunty bud')
else:
    print("sorry, you aren'nt old enough to drink")

# Boolean functions
x = 200
print(isinstance(x, int))   #isinstance(value, datatype checks data type
print(isinstance(x, bool))
print(isinstance(bool(x), bool)) # bool() converts to a boolean







