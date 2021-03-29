import os
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import sqlite3

# Import project modules
import phonebook_main
import phonebook_gui


def center_window(self, w, h):
    # Get user's screen w & h
    self.update_idletasks()
    screen_width = self.master.winfo_screenwidth()  # winfo is a tkinter method
    screen_height = self.master.winfo_screenheight()
    # Calculate x & y coordinates to paint app centered to user's screen
    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    center_geo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return center_geo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Really quit application?"):
        # Close app
        self.master.destroy()
        os._exit(0)


def create_db(self):
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_email TEXT, \
            col_phone TEXT \
            )")
        # Commit() changes & close the database conn
        conn.commit()
    conn.close()
    first_run(self)


def first_run(self):
    data = ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com')
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES \
            (?,?,?,?,?)""", ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com'))
            conn.commit()
    conn.close()


def count_records(cur):
    count = ''
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur, count


def onSelect(self, event):
    # Call the event from the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_email,col_phone FROM tbl_phonebook WHERE col_fullname = (?)""",
                       [value])
        varBody = cursor.fetchall()
        # Returns a tuple we can slice into 4 parts using data[] during iteration
        for data in varBody:
            self.txt_fname.delete(0, END)
            self.txt_fname.insert(0, data[0])
            self.txt_lname.delete(0, END)
            self.txt_lname.insert(0, data[1])
            self.txt_email.delete(0, END)
            self.txt_email.insert(0, data[2])
            self.txt_phone.delete(0, END)
            self.txt_phone.insert(0, data[3])


def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # Normalize the data returned
    var_fname = var_fname.strip()  # Remove blank spaces before & after the user's entry
    var_lname = var_lname.strip()
    var_fname = var_fname.title()  # Capitalize data
    var_fullname = ("{} {}".format(var_fname, var_lname))  # Combine names
    print("var_fullname: {}".format(var_fullname))
    var_email = self.txt_email.get().strip()
    var_phone = self.txt_phone.get().strip()
    if not '@' or not '.' in var_email:
        print('Incorrect email format!')
    # Require the user fill the complete form out
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0):
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cursor = conn.cursor()
            # Check database for existing user via fullname
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            check_name = count
            if check_name == 0:
                print('check_name: {}'.format(check_name))
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_email,col_phone) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_email,var_phone))
                self.lstList1.insert(END, var_fullname)
                onClear(self)   # Call function to clear text boxes
            else:
                messagebox.showerror("Name Error", "'{}' already has exists in the database! Please choose a different name".format(var_fullname))
                onClear(self)
            conn.commit()
            conn.close()
    else:
        messagebox.showerror("Missing Text Error", "All fields required.")


def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())  # Selected value from listbox
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        # Make sure this isn't the last record in db, throw error if it is
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permanently deleted from the database \n\nProceed with the deletion request?".format(var_select, var_select))
            if confirm:
                conn = sqlite3.connect('db_phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self)  # Function to clear all textboxes & the selected index of listbox
                onRefresh(self)  # Update listbox with changes
                conn.commit()
            else:
                confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot"
                                                                    "be deleted at this time. \n\nPlease add another "
                                                                    "record first before you can delete ({})".format(
                    var_select, var_select))


def onDeleted(self):
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_email.delete(0, END)
    self.txt_phone.delete(0, END)
    onRefresh(self)  # Update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass


def onClear(self):
    # Clear the text in these text-boxes
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_email.delete(0, END)
    self.txt_phone.delete(0, END)


def onRefresh(self):
    # Populate listbox, coinciding with the database
    self.lstList1.delete(0, END)
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0, str(item))
                i = i + 1
    conn.close()


def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0]
        var_value = self.lstList1.get(var_select)
    except:
        messagebox.showinfo("Missing selection",
                            "No name was selected from the list box. \nCancelling the Update request")
        return
    # User can only update phone and email values, for name changes the user will need to delete record & start over
    var_phone = self.txt_phone.get().strip()  # Normalize the data to maintain db integrity
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0):
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cur = conn.cursor()
            # Check if user's changes are already in DB
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0:  # If proposed changes are not already in the database, proceed
                response = messagebox.askokcancel("Update Request",
                                                  "The following changes ({}) and ({}) will be implemented for"
                                                  " ({}). \n\nProceed with the update request?".format(
                                                      var_phone, var_email, var_value))
                print(response)
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""Update tbl_phonebook SET col_phone = '{0}', col_email = '{1}' WHERE col_fullname = '{2}'""".format(var_phone, var_email, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({})".format(var_value))
            else:
                messagebox.showinfo("No changes detected",
                                    "Both ({}) and ({}) \nalready exist in the database for this name. \n\nYour "
                                    "update request has been cancelled".format(
                                        var_phone, var_email, var_value))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information",
                             "Please select a name from the list. \n Then edit the phone or email information")
    onClear(self)


if __name__ == '__main__':
    pass
