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
