# Python Ver:   3.9.2
#
# Author:       Nathan Skiles
#
# Purpose:      Create a script that will atomically copy files from src folder to destination folder, but only if the
#               file(s) were modified or created within the past 24 hours.
#
# Tested OS:    This code was written & tested to work with Windows 10

import os
import shutil
import stat
import time

# Set where the course of the files are
src = '/Users/nates/Documents/Tech Academy Projects/Python/fileTransferProject/folderA/'
# Set the destination path
dst = '/Users/nates/Documents/Tech Academy Projects/Python/fileTransferProject/folderB/'
files = os.listdir(src)


def timeModified(src, i):
    x = src + i     # Full file path
    modifyTime = time.time() - os.stat(x)[stat.ST_MTIME]    # Current time - time modified = time since modified
    return modifyTime


def sortFiles():
    for i in files:     # For each file in .listdir(src)
        if timeModified(src, i) <= 86400:       # If it's been less than 24 hours since the files was
            # Copy files (i) to their new destination
            shutil.copy2(src + i, dst)
            # print(timeModified(src, i))

if __name__ == '__main__':
    sortFiles()