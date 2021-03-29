# Python Ver:   3.9.2
#
# Author:       Nathan Skiles
#
# Purpose:
# Create the following:
#     A page title labeled “Student Tracking.”
#     A form to submit student information.
#       First name.
#       Last name.
#       Phone number.
#       Email.
#       Current course.
#       Submit button.
#     A section that displays the list of students with all the relevant information covered above.
#     A delete button that deletes selected students.
#
# Tested OS:    This code was written & tested to work with Windows 10

from tkinter import *
import tkinter as tk

import studentTracker_gui
import studentTracker_func


# Tkinter frame class
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame config
        self.master = master
        self.master.minsize(1000, 600)
        self.master.maxsize(1000, 600)
        studentTracker_func.centerWindow(self, 1000, 600)
        self.master.title('Student Tracking')
        self.master.configure(bg='#121212')

        # Check quit
        self.master.protocol('WM_DELETE_WINDOW', lambda: studentTracker_func.chkQuit(self))

        # Load GUI
        studentTracker_gui.load_gui(self)


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
