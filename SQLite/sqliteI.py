import sqlite3
# connection = sqlite3.connect('test_database.db')    # Connect to db, if none exists create one
# cur = connection.cursor()   # Create cursor object that we can use to interact with the DB
# cur.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))    # We have to change our input to a int to make sure its a valid age
personData = (firstName, lastName, age)

# with sqlite3.connect('test_database.db') as connection:
#     c = connection.cursor()
#     # Change age back into a string in order to concatenate with rest of the line
#     line = "INSERT INTO People VALUES ('" + firstName + "', '" + lastName + "', " + str(age) + ")"
#     c.execute(line)     # Execute our SQL statement formed above.

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)     # Insert a tuple to avoid misuse
    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
              (45, 'Flannery', "O'Connor"))     # Update row in table
