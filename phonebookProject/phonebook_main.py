# Python Ver:   3.9.2
#
# Author:       Nathan Skiles
#
# Purpose:      Phonebook Demo. Demonstrating OOP, TKinder GUI module, using Tkinter
#               Parent & Child relationships.
#
# Tested OS:    This code was written & tested to work with Windows 10

from tkinter import *
import tkinter as tk

# Include other phonebook modules
import phonebook_gui
import phonebook_func


# Frame will be the Tkinter frame class that our class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master
        self.master.minsize(500, 300)  # (Height, Width)
        self.master.maxsize(500, 300)
        # CenterWindow method that will center app on user's screen
        phonebook_func.center_window(self, 500, 300)
        self.master.title('Our Tkinter Phonebook Demo')
        self.master.configure(bg='#F0F0F0')
        # This protocol method is a built-in tkinter method to catch if
        #  the user clicks the upper corner, 'X' in Windows OS.
        self.master.protocol('WM_DELETE_WINDOW', lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load in GUI widgets from separate module
        phonebook_gui.load_gui(self)


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
