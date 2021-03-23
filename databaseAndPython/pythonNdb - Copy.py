
import sqlite3

conn  = sqlite3.connect('test.db')       # Hold our connection to database

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_persons( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_email TEXT \
            )')
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()         # Insert wild cards into columns in table persons
    cur.execute('INSERT INTO tbl_persons (col_fname, col_lname, col_email) VALUES (?, ?, ?)', \
                ('Sara', 'Jones', 'sarajones@gmail.com'))
    cur.execute('INSERT INTO tbl_persons (col_fname, col_lname, col_email) VALUES (?, ?, ?)', \
                ('Kyle', 'Bacon', 'kbake@gmail.com'))
    cur.execute('INSERT INTO tbl_persons (col_fname, col_lname, col_email) VALUES (?, ?, ?)', \
                ('Mike', 'Jones', 'immjones@gmail.com'))
    conn.commit()                # commits changes to DB
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Sara' ")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {} \nLast Name: {} \nEmail: {}".format(item[0], item[1], item[2])
    print(msg)
    
        
