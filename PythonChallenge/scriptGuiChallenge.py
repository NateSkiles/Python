from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define Frame
        self.master = master
        self.master.minsize(500, 200)
        self.master.maxsize(500, 200)
        self.master.title('Check Files')

        # UI
        self.btn_browse1 = tk.Button(self.master, text='Browse...', width=15)
        self.btn_browse1.grid(row=1, column=0, padx=(10, 10), pady=(40, 10), sticky=W)
        self.btn_browse2 = tk.Button(self.master, text='Browse...', width=15)
        self.btn_browse2.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky=W)
        self.btn_checkFiles = tk.Button(self.master, text='Check for Files...', height=2, width=15)
        self.btn_checkFiles.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky=S + E)
        self.btn_closeProgram = tk.Button(self.master, text='Close Program', height=2, width=15)
        self.btn_closeProgram.grid(row=3, column=1, padx=(50, 0), pady=(0, 0), sticky=S+E)

        self.lbl_entry1 = tk.Entry(self.master, text='', width=50)
        self.lbl_entry1.grid(row=1, column=1, padx=(10, 10), pady=(40, 10), sticky=W)
        self.lbl_entry2 = tk.Entry(self.master, text='', width=50)
        self.lbl_entry2.grid(row=2, column=1, padx=(10, 10), pady=(10, 10), sticky=W)


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
