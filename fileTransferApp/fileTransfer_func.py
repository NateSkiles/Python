from tkinter import filedialog as fd
from tkinter import messagebox as mb
import fileTransfer_GUI
import os
import shutil
import stat
import time


# Functions
def browseDir(x):
    dirName = fd.askdirectory()     # When function is called open file browser, save dir selected as dirName
    if dirName:                     # If dirName exists
        x.set(dirName)              # Use .set() to modify the StringVar() that was set as Entry text


def sortFiles():
    src = fileTransfer_GUI.strVar.get() + '/'       # Set src & dst = to user chosen dir, add forward slash so filepath
    dst = fileTransfer_GUI.strVar2.get() + '/'      # is correctly concatenated to filename
    files = os.listdir(src)
    for i in files:                                 # For each file in .listdir(src)
        if timeModified(src, i) <= 86400:           # If it's been less than 24 hours since the files was
            # Copy files (i) to their new destination
            shutil.copy2(src + i, dst)
            print('File: ' + i + ' copied')


def timeModified(src, i):
    x = src + i     # Full file path
    modifyTime = time.time() - os.stat(x)[stat.ST_MTIME]    # Current time - time modified = time since modified
    return modifyTime


def closeProgram(self):
    if mb.askokcancel('Quit Program', 'Would you really like to quit the application?'):
        # Close app
        self.master.destroy()
        os._exit(0)
