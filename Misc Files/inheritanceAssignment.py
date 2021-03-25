class Computer:  # Create class: Computer
    brand = ''
    CPU = ''
    GPU = ''
    storage = ''
    RAM = ''

    def __init__(self, brand, CPU, GPU, storage,  # Initializing our class so was can store values in its attributes
                 RAM):
        self.brand = brand
        self.CPU = CPU
        self.GPU = GPU
        self.storage = storage
        self.RAM = RAM

    def config(self):  # Return a printable representation of our object
        return '\n'.join(['Brand: ' + self.brand, 'CPU: ' + self.CPU, 'GPU: ' + self.GPU, 'Storage: ' + self.storage,
                          'RAM: ' + self.RAM + '\n'])


# Child class of Computer class
class mobilePhone(Computer):
    batterySize = ''
    screenSize = ''

    def __init__(self, brand, storage, batterySize, screenSize):
        self.brand = brand
        self.storage = storage
        self.batterySize = batterySize
        self.screenSize = screenSize

    def config(self):
        return '\nBrand: {}\nStorage: {}\nBattery Size: {}\nScreen Size: {}\n'.format(self.brand, self.storage,
                                                                                      self.batterySize, self.screenSize)


# Child class of Computer class
class gameConsole(Computer):
    numberOfControllers = 0
    color = ''

    def __init__(self, brand, storage, numberOfControllers, color):
        self.brand = brand
        self.storage = storage
        self.numberOfControllers = numberOfControllers
        self.color = color

    def config(self):
        return '\nBrand: {}\nStorage: {}\nNumber of Controllers: {}\nConsole Color: ' \
               '{}'.format(self.brand, self.storage, self.numberOfControllers, self.color)


# Create our computer object and print that object
myPC = Computer('Dell', '8700k', 'GTX 1080', '1TB', '8GB')
myPhone = mobilePhone('Apple', '16 GB', '2,815 mAh', '16-inch')
myConsole = gameConsole('XBOX', '1TB', 2, 'white')
print(Computer.config(myPC), mobilePhone.config(myPhone), gameConsole.config(myConsole))
