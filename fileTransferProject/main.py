# Python Ver:   3.9.2
#
# Author:       Nathan Skiles
#
# Purpose:      Your employer wants a program to move all their text files (with a .txt file extension) from one
#               folder to another with the click of a button. On your desktop you will have two new folders, one
#               called Folder A and another called Folder B. You will need to move text files from Folder A to Folder B.
#
# Tested OS:    This code was written & tested to work with Windows 10

import shutil
import os

# Set where the course of the files are
source = 'C:/Users/nates/Documents/Tech Academy Projects/Python/fileTransferProject/folderA/'
# Set the destination path
destination = 'C:/Users/nates/Documents/Tech Academy Projects/Python/fileTransferProject/folderB/'
files = os.listdir(source)

for i in files:
    # Move files (i) to their new destination
    shutil.move(source+i, destination)
