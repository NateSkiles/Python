# Python Ver:   3.9.2
#
# Author:       Nathan Skiles
#
# Purpose:      Your employer wants a program to move all their text files (with a .txt file extension) from one
#               folder to another with the click of a button. On your desktop you will have two new folders, one
#               called Folder A and another called Folder B. You will need to move text files from Folder A to Folder B.
#
# Tested OS:    This code was written & tested to work with Windows 10

from tkinter import *
import tkinter as tk
import fileTransfer_GUI


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define Frame
        self.master = master
        self.master.minsize(500, 200)
        self.master.maxsize(500, 200)
        self.master.title('Check Files')

        # Load GUI
        fileTransfer_GUI.loadGui(self)


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
