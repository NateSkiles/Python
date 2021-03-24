import sqlite3

conn = sqlite3.connect('dbAssignment.db')

fileList = ('information.dox', 'hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhono.jpg')
y = '.txt'

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files( \
                    FileID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_fileName TEXT)')


for file in fileList:
    if file.endswith(y):
        with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files (col_fileName) VALUES (?)", (file,))
                conn.commit()
        print(file)
        conn.close
        

        
    
