from tkinter import *
import tkinter as tk
import fileTransfer_func


def loadGui(self):
    # Global Variables
    global strVar
    global strVar2
    strVar = StringVar()
    strVar2 = StringVar()

    # UI
    self.btn_browse1 = tk.Button(self.master, text='Source', width=15,
                                 command=lambda: fileTransfer_func.browseDir(strVar))
    self.btn_browse1.grid(row=1, column=0, padx=(10, 10), pady=(40, 10), sticky=W)
    self.btn_browse2 = tk.Button(self.master, text='Destination', width=15,
                                 command=lambda: fileTransfer_func.browseDir(strVar2))
    self.btn_browse2.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky=W)
    self.btn_checkFiles = tk.Button(self.master, text='Check for Files...', height=2, width=15,
                                    command=lambda: fileTransfer_func.sortFiles())
    self.btn_checkFiles.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky=S + E)
    self.btn_closeProgram = tk.Button(self.master, text='Close Program', height=2, width=15,
                                      command=lambda: fileTransfer_func.closeProgram(self))
    self.btn_closeProgram.grid(row=3, column=1, padx=(50, 0), pady=(0, 0), sticky=S + E)

    self.lbl_entry1 = tk.Entry(self.master, text=strVar, width=50)
    self.lbl_entry1.grid(row=1, column=1, padx=(10, 10), pady=(40, 10), sticky=W)
    self.lbl_entry2 = tk.Entry(self.master, text=strVar2, width=50)
    self.lbl_entry2.grid(row=2, column=1, padx=(10, 10), pady=(10, 10), sticky=W)
