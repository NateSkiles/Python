# Create an absolute file path join(path, *paths)

import os

fName = 'test.txt'

fPath = 'C:\\Users\\nates\\Documents\\Tech Academy Projects\\Python\\os'

abPath = os.path.join(fPath, fName)
print(abPath)

if os.path.exists(abPath) == True:
    print('Path Exists')
else:
    print('Path does not exist')
