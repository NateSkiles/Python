import sqlite3

nerds = (('Jean-Bapiste', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100),
         ("'Ak'not", "Mangalore", -5))

with sqlite3.connect(':memory:') as conn:
    cur = conn.cursor()
    # Create Database table in RAM named Roster that includes fields: 'Name', 'Species', & 'IQ'
    cur.execute("CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, IQ INT)")
    cur.executemany("INSERT INTO Roster VALUES(?, ?, ?)", nerds)
    # Update Korben's Race to Human
    cur.execute("UPDATE ROSTER SET Species='Human' WHERE Name='Korben Dallas'")
    # Display Names & IQ of the Humans in the table
    cur.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    for row in cur.fetchall():
        print(row)
