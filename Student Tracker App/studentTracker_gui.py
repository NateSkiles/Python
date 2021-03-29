from tkinter import *
import tkinter as tk

import studentTracker_func


def load_gui(self):
    self.lbl_fname = tk.Label(self.master, bg='#121212', fg='#fff', font='Segoe', text='First Name: ')
    self.lbl_fname.grid(row=0, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_lname = tk.Label(self.master, bg='#121212', fg='#fff', font='Segoe', text='Last Name: ')
    self.lbl_lname.grid(row=4, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_email = tk.Label(self.master, bg='#121212', fg='#fff', font='Segoe', text='Email: ')
    self.lbl_email.grid(row=7, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_phone = tk.Label(self.master, bg='#121212', fg='#fff', font='Segoe', text='Phone: ')
    self.lbl_phone.grid(row=10, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_ccourse = tk.Label(self.master, bg='#121212', fg='#fff', font='Segoe', text='Current Course: ')
    self.lbl_ccourse.grid(row=13, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)

    self.txt_fname = tk.Entry(self.master, text='')
    self.txt_fname.grid(row=1, column=0, rowspan=2, columnspan=2, padx=(40, 50), pady=(10, 10), sticky=N + E + W)
    self.txt_lname = tk.Entry(self.master, text='')
    self.txt_lname.grid(row=5, column=0, rowspan=2, columnspan=2, padx=(40, 50), pady=(10, 10), sticky=N + E + W)
    self.txt_email = tk.Entry(self.master, text='')
    self.txt_email.grid(row=8, column=0, rowspan=2, columnspan=2, padx=(40, 50), pady=(10, 10), sticky=N + E + W)
    self.txt_phone = tk.Entry(self.master, text='')
    self.txt_phone.grid(row=11, column=0, rowspan=2, columnspan=2, padx=(40, 50), pady=(10, 10), sticky=N + E + W)
    self.txt_ccourse = tk.Entry(self.master, text='')
    self.txt_ccourse.grid(row=14, column=0, rowspan=2, columnspan=2, padx=(40, 50), pady=(10, 10), sticky=N + E + W)

    self.btn_submit = tk.Button(self.master, width=12, height=3, text='Submit')
    self.btn_submit.grid(row=16, column=0, pady=(80, 0), columnspan=1)

    studentTracker_func.create_db(self)
    studentTracker_func.onRefresh(self)


if __name__ == '__main__':
    pass
