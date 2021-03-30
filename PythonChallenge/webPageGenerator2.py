# Python Ver:   3.9.2
#
# Author:       Nathan Skiles
#
# Purpose:      Your task is to create a GUI with Tkinter that will enable the users to set the
#                   body text for a newly-created web page. There should also be a control in the
#                   GUI that initiates the process of making the new web page.
#
# Tested OS:    This code was written & tested to work with Windows 10

import webbrowser
import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(325, 150)
        self.master.maxsize(325, 150)
        self.master.title('Web Page Gene')

        self.lbl_userInput = tk.Label(self.master, text='What would you like the body of your webpage to say : ')
        self.lbl_userInput.grid(row=0, column=0, sticky=N+W, pady=(10, 10), padx=(5, 5))
        self.entry_userInput = tk.Entry(self.master, text='')
        self.entry_userInput.grid(row=1, column=0, columnspan=2, rowspan=3, ipady=4)

        self.btn_userInput = tk.Button(self.master, text='Submit', width=10, height=2, command=lambda: htmlGene(self))
        self.btn_userInput.grid(row=4, column=0, padx=(5, 5), pady=(10, 10))

        def htmlGene(self):
            userEntry = self.entry_userInput.get()
            x = "<html><body><h1>" + userEntry + "</h1></body></html> "
            f = open("SummerSale.html", "w")
            f.write(x)
            f.close()
            webbrowser.open("SummerSale.html")




if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
