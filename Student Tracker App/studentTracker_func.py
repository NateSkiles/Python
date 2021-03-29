import os
from tkinter import messagebox
from tkinter import *
import sqlite3



def chkQuit(self):
    if messagebox.askokcancel('Quit Program', 'Would you really like to quit the application?'):
        # Close app
        self.master.destroy()
        os._exit(0)


def centerWindow(self, w, h):
    # Get user's screen h&w
    self.update_idletasks()
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    center_geo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))

    return center_geo


def create_db(self):
    conn = sqlite3.connect('studentTacker.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_studentTracker( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_email TEXT, \
            col_phone TEXT,  \
            col_ccourse TEXT \
            )")
        conn.commit()
    conn.close()
    test_entry(self)

def test_entry(self):
    data = ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com')
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_studentTracker (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES \
                (?,?,?,?,?)""", ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com'))
            conn.commit()
    conn.close()

def count_recourds(self):
    count = ''
    cur.execute("""SELECT COUNT(*) FROM tbl_studentTracker""")
    count = cur.fetchone()[0]
    return cur, count


def onRefresh(self):
    return None