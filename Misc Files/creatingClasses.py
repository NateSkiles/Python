class User:
    name = 'No name provided'  # Define the attributes of the class
    email = ''
    password = '12345abcd'
    account = 0

    def login(self):  # Define the methods of the class
        entry_email = input('Enter your email: ')
        entry_password = input('Enter your password: ')
        if entry_email == self.email and entry_password == self.password:
            print('Welcome back, {}'.format(self.name))
        else:
            print('You are not authorized for this page')

    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account


class Employee(User):
    base_pay = 11.00
    department = 'General'


class Customer(User):
    mailing_address = ''
    mailing_list = True


# Outside of the class you would create an instance of the user class
new_user = User("John Deere", "jdeere@outlook.com", "p@ssword", 1234)
# Call the login method using the new object
new_user.login()
