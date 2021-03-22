# loop to i = 10
i = 0
for i in range(10):
    print('{} iteration through the loop.'.format(i))
    i += 1 # i = i + 1

# my loop
i = 0
while i < 6:
    print(i)
    if i == 3:
        break       # break out of while loop
    i += 1


while i < 6:
  i += 1
  if i == 3:
    continue    # continue while loop
  print(i)

  # else statement in while loops
i = 1
while  i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


"""
Execute a for loop.

Use the break statement within a for loop.

Use the continue statement within a for loop.

Use the range() function within a for loop.        

Use the else keyword within a for loop.
"""

# for loop
colors = ["red", "yellow", "green"]
for x in colors:
    print(x)

for x in colors:
    print(x)
    if x == 'yellow':
        break

for x in colors:
    print(x)
    if x == 'yellow':
        continue

# range() function in for loop
for x in range(10):
    print(x)
